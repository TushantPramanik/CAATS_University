"""Small CAATS counselling portal using only Python's standard library."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from http.cookies import SimpleCookie
from pathlib import Path
import hashlib
import hmac
import json
import math
import os
import re
import secrets
import sqlite3
import time
import urllib.parse

ROOT = Path(__file__).parent
DB_PATH = ROOT / "caats.sqlite3"
SESSIONS = {}

SKILLS = ["Content Creation", "Video Editing", "Digital Marketing", "Entrepreneurship", "Programming", "Graphic Designing"]
MASTERS = ["AI and ML", "Technical Leadership", "System Design", "Fundamentals of Cloud Computing"]
SCHOOL_GOALS = ["Boards", "Olympiad"]
BSC = ["Physics", "Mathematics", "Statistics", "Economics", "Computer Science", "Chemistry", "Electronics", "Biotechnology"]
BCA = ["Artificial Intelligence and Machine Learning", "Cloud Computing", "Cyber Security", "Software Development", "Internet of Things"]
INTERESTS = ["Programming", "Artificial Intelligence", "Security & Hacking", "Data Analysis", "Electronics", "Machines & Automobiles", "Construction & Design", "Electrical Systems", "Production", "Agricultural", "Food", "Printing"]

BTECH_GROUPS = {
    "top": {
        "Programming": ["CORE CSE", "CSE AI/ML", "CSE Data Science", "CSE Cyber Security", "Information Technology", "CSE IOT"],
        "Artificial Intelligence": ["CORE CSE", "CSE (AI & ML)"],
        "Security & Hacking": ["CORE CSE", "CSE Cyber Security", "Information Security"],
        "Data Analysis": ["CSE Data Science", "Big Data Analytics", "CORE CSE"],
        "Electronics": ["Electronics & Communication Engineering (ECE)"],
        "Machines & Automobiles": ["Mechanical Engineering", "Automobile Engineering"],
        "Construction & Design": ["Civil Engineering"],
        "Electrical Systems": ["Electrical Engineering (EE)", "Electrical & Electronics Engineering (EEE)"]
    },
    "upper": {
        "Programming": ["CSE Data Science", "CSE Cyber Security", "Information Technology", "CSE IOT"],
        "Security & Hacking": ["CORE CSE", "CSE Cyber Security", "Information Security"],
        "Data Analysis": ["CSE Data Science", "Big Data Analytics", "CORE CSE"],
        "Electronics": ["Electronics & Communication Engineering (ECE)"],
        "Machines & Automobiles": ["Mechanical Engineering", "Automobile Engineering"],
        "Construction & Design": ["Civil Engineering"],
        "Electrical Systems": ["Electrical Engineering (EE)", "Electrical & Electronics Engineering (EEE)"]
    },
    "middle": {
        "Data Analysis": ["CSE Data Science", "Big Data Analytics", "CORE CSE"],
        "Electronics": ["Electronics & Communication Engineering (ECE)"],
        "Machines & Automobiles": ["Mechanical Engineering", "Automobile Engineering"],
        "Construction & Design": ["Civil Engineering"],
        "Electrical Systems": ["Electrical Engineering (EE)", "Electrical & Electronics Engineering (EEE)"]
    },
    "lower": {
        "Electronics": ["Electronics & Communication Engineering (ECE)"],
        "Machines & Automobiles": ["Mechanical Engineering", "Automobile Engineering"],
        "Construction & Design": ["Civil Engineering"],
        "Electrical Systems": ["Electrical Engineering (EE)", "Electrical & Electronics Engineering (EEE)"]
    },
    "entry": {
        "Machines & Automobiles": ["Mechanical Engineering", "Automobile Engineering"],
        "Construction & Design": ["Civil Engineering"],
        "Electrical Systems": ["Electrical Engineering (EE)", "Electrical & Electronics Engineering (EEE)"],
        "Production": ["Production Engineering"],
        "Agricultural": ["Agricultural Engineering"]
    },
    "foundation": {
        "Agricultural": ["Agricultural Engineering"],
        "Food": ["Food Technology"],
        "Printing": ["Printing Engineering"]
    }
}

EMAIL_REGEX = re.compile(r"^[^@\s]+@[^@\s]+\.[a-zA-Z0-9-]{2,}$")

def connect():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys=ON")
    return db

def init_db():
    with connect() as db:
        db.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY, email TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL,
            name TEXT NOT NULL DEFAULT '', profession TEXT NOT NULL DEFAULT '', age_band TEXT NOT NULL DEFAULT '',
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            answers TEXT NOT NULL, result TEXT NOT NULL, created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        """)

def json_response(handler, data, status=None):
    if status is None:
        status = data.get("status", 200) if isinstance(data, dict) else 200
    body = json.dumps(data).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.send_header("Cache-Control", "no-store")
    handler.send_header("X-Content-Type-Options", "nosniff")
    handler.end_headers()
    handler.wfile.write(body)

def user_for(handler):
    cookie = SimpleCookie(handler.headers.get("Cookie", ""))
    morsel = cookie.get("caats_session")
    if not morsel:
        return None
    session = SESSIONS.get(morsel.value)
    if not session or session[1] < time.time():
        SESSIONS.pop(morsel.value, None)
        return None
    with connect() as db:
        row = db.execute("SELECT id,email,name,profession,age_band FROM users WHERE id=?", (session[0],)).fetchone()
    return dict(row) if row else None

def set_session(handler, user_id):
    token = secrets.token_urlsafe(32)
    SESSIONS[token] = (user_id, time.time() + 60 * 60 * 24 * 7)
    handler.send_header("Set-Cookie", f"caats_session={token}; HttpOnly; SameSite=Lax; Path=/; Max-Age=604800")

def error(message, status=400):
    return {"error": message, "status": status}

def validate_score(val, name="percentage"):
    if val is None or isinstance(val, bool) or not isinstance(val, (int, float)):
        raise ValueError(f"Enter a valid {name} from 0 to 100.")
    if not math.isfinite(val) or val < 0 or val > 100:
        raise ValueError(f"{name.capitalize()} must be between 0 and 100.")
    return float(val)

def recommendation(a):
    profession = a.get("profession")
    age = a.get("age_band")
    if profession not in ("Student", "Working", "Other") or age not in ("Under 13", "13–14", "14–15", "15–16", "16–17", "17+"):
        raise ValueError("Choose a valid profession and age band to continue.")

    if profession == "Working" and age != "17+":
        raise ValueError("The source project limits the work pathway to age 17+.")

    pathway = a.get("pathway")

    # Other Pathway: strictly skills only
    if profession == "Other":
        if pathway is not None and pathway != "skills":
            raise ValueError("Other visitors can only choose the skills pathway.")
        option = a.get("choice")
        if option not in SKILLS:
            raise ValueError("Choose one of the listed skills.")
        return {"title": option, "category": "Skill pathway", "detail": "This skill choice follows the original project’s skills menu."}

    # Working Pathway: skills or 4-hour master class
    if profession == "Working":
        if pathway not in ("skills", "master"):
            raise ValueError("Choose skills or a 4-hour master class.")
        if pathway == "skills":
            option = a.get("choice")
            if option not in SKILLS:
                raise ValueError("Choose one of the listed skills.")
            return {"title": option, "category": "Skill pathway", "detail": "This skill choice follows the original project’s skills menu."}
        else:
            option = a.get("choice")
            if option not in MASTERS:
                raise ValueError("Choose a short master class.")
            return {"title": option, "category": "Master class · 4 hours", "detail": "This course choice follows the original project’s master class menu."}

    # Student Pathway
    if profession != "Student":
        raise ValueError("Choose a valid pathway to continue.")

    if age == "Under 13":
        if pathway is not None and pathway != "skills":
            raise ValueError("Under-13 students can only choose the skills pathway in the source project.")
        option = a.get("choice")
        if option not in SKILLS:
            raise ValueError("Choose one of the listed skills.")
        return {"title": option, "category": "Skill pathway", "detail": "Under-13 students were routed to skills in the source project."}

    school_age = {"13–14": "Class 9", "14–15": "Class 10", "15–16": "Class 11", "16–17": "Class 12"}
    if age in school_age:
        if pathway not in ("school", "skills"):
            raise ValueError(f"For age group {age}, choose the school or skills pathway.")
        if pathway == "school":
            goal = a.get("choice")
            if goal not in SCHOOL_GOALS:
                raise ValueError("Choose Boards or Olympiad.")
            return {"title": f"{school_age[age]} · {goal}", "category": "School pathway", "detail": "School class and goal are taken from the age-based flow in the source."}
        else:
            option = a.get("choice")
            if option not in SKILLS:
                raise ValueError("Choose one of the listed skills.")
            return {"title": option, "category": "Skill pathway", "detail": "This skill choice follows the original project’s skills menu."}

    # Student age 17+
    if age != "17+":
        raise ValueError("Invalid age band specified.")

    if pathway not in ("college", "skills"):
        raise ValueError("For age 17+, choose college or skills.")

    if pathway == "skills":
        option = a.get("choice")
        if option not in SKILLS:
            raise ValueError("Choose one of the listed skills.")
        return {"title": option, "category": "Skill pathway", "detail": "This skill choice follows the original project’s skills menu."}

    # College pathway: Validate percentage
    mark = validate_score(a.get("percentage"), "class 12 percentage")
    if mark < 33:
        return {"title": "No college admission path defined", "category": "Eligibility result", "detail": "The source project says admission is not possible below 33% in class 12."}

    course = a.get("course")
    if course is None:
        raise ValueError("Choose a college course.")

    if course not in ("BTech", "BSc", "BCA", "Diploma"):
        raise ValueError("Choose a valid college course (BTech, BSc, BCA, or Diploma).")

    eligible_courses = ["BTech", "BSc", "BCA", "Diploma"] if mark >= 75 else ["BSc", "BCA", "Diploma"] if mark >= 55 else ["BSc", "Diploma"] if mark >= 40 else ["Diploma"] if mark >= 33 else []
    if course not in eligible_courses:
        raise ValueError(f"That course is not offered for {mark:g}% in the source project. Available choices: " + (", ".join(eligible_courses) if eligible_courses else "none; the source says admission is not possible below 33%."))

    warnings = []

    # Diploma Course
    if course == "Diploma":
        warnings.append("The diploma rules are unavailable: the referenced K_diploma_clg_dep.py file was not included.")
        return {"title": "Diploma pathway", "category": "College pathway", "detail": "Diploma selected. Eligibility and courses need the original diploma module to verify.", "warnings": warnings}

    # BSc / BCA Courses
    if course in ("BSc", "BCA"):
        if course == "BSc":
            if mark >= 75: options = BSC
            elif mark >= 70: options = BSC[1:]
            elif mark >= 65: options = BSC[2:]
            elif mark >= 60: options = BSC[3:]
            elif mark >= 55: options = BSC[4:]
            elif mark > 40: options = BSC[6:]
            else: options = ["Biotechnology"]
            if mark == 40:
                warnings.append("At exactly 40%, the source branches conflict: a >=40 tier offers Biotechnology, while a later <=40 condition says not eligible.")
        else:
            if mark >= 80: options = BCA
            elif 75 <= mark < 80: options = BCA[1:]
            elif 65 <= mark < 70: options = BCA[2:]
            elif 60 <= mark < 65: options = BCA[3:]
            elif 55 <= mark < 60: options = BCA[4:]
            else:
                options = []
                warnings.append("The BCA source does not define recommendations for 70% to below 75%.")

        selected = a.get("choice")
        if selected not in options:
            if not options:
                return {"title": "No BCA recommendation defined", "category": "Needs review", "detail": "The source has no BCA branch tier for this percentage.", "warnings": warnings}
            raise ValueError("Select one of the options listed for this score: " + ", ".join(options))
        return {"title": selected, "category": f"{course} recommendation", "detail": f"Options follow the source project’s {course} percentage tiers.", "warnings": warnings}

    # BTech Course: Validate CAATS JEE Percentile
    score = validate_score(a.get("jee"), "CAATS JEE percentile")
    if score >= 85: bands = "top"
    elif 75 <= score <= 84: bands = "upper"
    elif 65 <= score <= 74: bands = "middle"
    elif 55 <= score <= 64: bands = "lower"
    elif 45 <= score <= 54: bands = "entry"
    elif 35 <= score <= 44: bands = "foundation"
    else:
        return {"title": "No BTech recommendation defined", "category": "Needs review", "detail": "The source has no BTech branch for this score."}

    if score != int(score):
        warnings.append("The source uses whole-number percentile bands; decimal percentile handling is not defined.")

    i = a.get("interest")
    if bands == "upper" and i == "Programming":
        raise ValueError("Programming is listed as an interest for 75–84 in the source, but its BTech branch-choice block is missing.")

    choices = BTECH_GROUPS[bands].get(i, [])
    if not choices:
        allowed = sorted(BTECH_GROUPS[bands])
        raise ValueError("Choose an interest available for your score: " + ", ".join(allowed))

    selected = a.get("choice")
    if selected not in choices:
        raise ValueError("Select a branch listed for your interest: " + ", ".join(choices))

    return {"title": selected, "category": "BTech recommendation", "detail": f"Based on {score:g} CAATS JEE percentile and interest in {i}.", "warnings": warnings}

class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_): pass

    def body(self):
        n = int(self.headers.get("Content-Length", "0"))
        if n > 100_000:
            raise ValueError("Request is too large.")
        return json.loads(self.rfile.read(n) or b"{}")

    def do_GET(self):
        path = urllib.parse.urlparse(self.path).path
        if path == "/":
            data = (ROOT / "index.html").read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return

        if path in ("/style.css", "/app.js"):
            data = (ROOT / path[1:]).read_bytes()
            typ = "text/css" if path.endswith(".css") else "text/javascript"
            self.send_response(200)
            self.send_header("Content-Type", typ + "; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return

        if path == "/api/me":
            user = user_for(self)
            if not user:
                return json_response(self, {"user": None, "history": []})
            with connect() as db:
                rows = db.execute("SELECT id,result,created_at FROM recommendations WHERE user_id=? ORDER BY id DESC", (user["id"],)).fetchall()
            return json_response(self, {"user": user, "history": [{**dict(r), "result": json.loads(r["result"])} for r in rows]})

        return json_response(self, error("Not found", 404), 404)

    def do_POST(self):
        try:
            data = self.body()
            path = urllib.parse.urlparse(self.path).path

            if path in ("/api/register", "/api/login"):
                email = str(data.get("email", "")).strip().lower()
                password = str(data.get("password", ""))

                if not email or len(email) > 254 or not EMAIL_REGEX.match(email):
                    return json_response(self, error("Enter a valid email address (e.g. student@caats.edu)."))

                if not password:
                    return json_response(self, error("Enter your password."))

                with connect() as db:
                    if path.endswith("register"):
                        if len(password) < 8 or len(password) > 128:
                            return json_response(self, error("Password must be between 8 and 128 characters."))
                        name = str(data.get("name", "")).strip()[:80]
                        if not name:
                            return json_response(self, error("Enter your name."))

                        salt = secrets.token_bytes(16)
                        hashed = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 240_000)
                        try:
                            cur = db.execute("INSERT INTO users(email,password_hash,name) VALUES(?,?,?)", (email, salt.hex() + ":" + hashed.hex(), name))
                            uid = cur.lastrowid
                        except sqlite3.IntegrityError:
                            return json_response(self, error("An account with this email already exists."))
                    else:
                        row = db.execute("SELECT id,password_hash FROM users WHERE email=?", (email,)).fetchone()
                        if not row:
                            return json_response(self, error("Email or password is incorrect.", 401), 401)
                        salt_hex, digest = row["password_hash"].split(":", 1)
                        actual = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), bytes.fromhex(salt_hex), 240_000).hex()
                        if not hmac.compare_digest(actual, digest):
                            return json_response(self, error("Email or password is incorrect.", 401), 401)
                        uid = row["id"]

                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Cache-Control", "no-store")
                set_session(self, uid)
                self.end_headers()
                self.wfile.write(b'{"ok":true}')
                return

            if path == "/api/logout":
                cookie = SimpleCookie(self.headers.get("Cookie", ""))
                m = cookie.get("caats_session")
                if m:
                    SESSIONS.pop(m.value, None)
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Set-Cookie", "caats_session=; HttpOnly; SameSite=Lax; Path=/; Max-Age=0")
                self.end_headers()
                self.wfile.write(b'{"ok":true}')
                return

            if path == "/api/profile":
                user = user_for(self)
                if not user:
                    return json_response(self, error("Please log in first.", 401), 401)
                profession, age = data.get("profession"), data.get("age_band")
                if profession not in ("Student", "Working", "Other") or age not in ("Under 13", "13–14", "14–15", "15–16", "16–17", "17+"):
                    return json_response(self, error("Choose a valid profession and age band."))
                if profession == "Working" and age != "17+":
                    return json_response(self, error("The source project limits the work pathway to age 17+."))
                with connect() as db:
                    db.execute("UPDATE users SET profession=?,age_band=? WHERE id=?", (profession, age, user["id"]))
                return json_response(self, {"ok": True})

            if path == "/api/recommend":
                user = user_for(self)
                if not user:
                    return json_response(self, error("Please log in to save your counselling result.", 401), 401)
                answers = data.get("answers", {})
                result = recommendation(answers)
                with connect() as db:
                    db.execute("UPDATE users SET profession=?,age_band=? WHERE id=?", (answers.get("profession", ""), answers.get("age_band", ""), user["id"]))
                    cur = db.execute("INSERT INTO recommendations(user_id,answers,result) VALUES(?,?,?)", (user["id"], json.dumps(answers), json.dumps(result)))
                return json_response(self, {"id": cur.lastrowid, "result": result})

            return json_response(self, error("Not found", 404), 404)
        except (ValueError, json.JSONDecodeError) as e:
            return json_response(self, error(str(e) or "Check your answers."))
        except Exception:
            return json_response(self, error("Something went wrong. Please try again.", 500), 500)

if __name__ == "__main__":
    init_db()
    port = int(os.environ.get("PORT", "8000"))
    print(f"CAATS University is running at http://127.0.0.1:{port}")
    ThreadingHTTPServer(("127.0.0.1", port), Handler).serve_forever()
