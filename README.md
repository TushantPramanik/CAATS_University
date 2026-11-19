# CAATS University Counselling & Admissions Portal

A beginner-friendly, full-stack academic counselling and admissions web portal for CAATS University, evolved from the original Python console project. It combines an authentic university-inspired aesthetic with strict rule-based counselling, robust input validation, and an interactive course enrollment payment gateway.

Built entirely using Python's standard library (`http.server`, `sqlite3`, `hashlib`, `json`), vanilla HTML5/CSS3, and modern JavaScript with **zero external packages or runtime dependencies**.

---

![CAATS University Homepage](assets/Screenshot%202026-11-20%20000811.png)

---

## Key Features

### 🎓 Rule-Verified Academic Counselling
- **Personalized Pathway Navigation**: Guided flows tailored for school students, college applicants, working learners, and independent skill seekers.
- **B.Tech Engineering**: Six CAATS JEE percentile tiers (Top, Upper, Middle, Lower, Entry, Foundation) and branch allocations mapped from `F_Btech_clg_dep.py`.
- **BCA (Computing)**: Tiered software and IT specializations (AI/ML, Cloud Computing, Cyber Security, Software Development, IoT) from `I_Bca_clg_dep.py`.
- **B.Sc Sciences**: Eight pure and applied science subjects mapped from `G_Bsc_clg_dep.py`.
- **Diploma Engineering**: Fully integrated from `K_diploma_clg_dep.py` with Class 10 percentage verification (minimum 35%) and 5 engineering disciplines (Civil, Mechanical, Electrical, Electronics & Communication, Automobile).
- **School & Career Tracks**: Class 9–12 Boards/Olympiad preparation from `C_school_dep.py`, 6 practical skill tracks, and 4-hour executive master classes from `D_work_dep.py`.

### 💳 Interactive Course Payment Gateway
- **Flexible Tuition Schedules**: Semester-wise, Half-Yearly, Yearly (with annual value savings), and Full Program payments mapped from `L_bat_prch.py`.
- **Live Virtual Card Preview**: Dynamic credit/debit card mockup with real-time 16-digit formatting (`XXXX XXXX XXXX XXXX`), card brand detection (Visa, Mastercard, RuPay, Amex), expiry masks, and cardholder synchronization.
- **Multiple Payment Channels**: Cards, interactive simulated UPI QR code / VPA address, and Net Banking across major institutions.
- **3D-Secure 2.0 Simulation**: Realistic bursar handshake and batch verification sequence.
- **Digital Bursar Receipts**: Official fee receipt generation with unique transaction IDs (`CAATS-TXN-...`), timestamp, student details, and one-click printable layout.

### 🛡️ Robust Validation & Source Gap Transparency
- **Strict Input Constraints**: Backend and frontend enforcement rejecting negative numbers, scores over 100, non-finite values (`NaN`, `Infinity`), boolean types, and non-numeric characters without silent clamping.
- **Course Eligibility Verification**: Prevents unauthorized degree applications prior to qualification checks.
- **Documented Source Edge Cases**: Explicit notices for known source conflicts and gaps documented in [web-app/SOURCE_RULES.md](web-app/SOURCE_RULES.md):
  - Conflicting BSc 40% Biotechnology rule
  - BCA 70% to below 75% unhandled band
  - Whole-number B.Tech JEE percentile bands
  - Diploma Class 12 33% vs 34% threshold boundary
  - Missing B.Tech Programming branch block at 75–84

### 🔒 Security & Student Workspace
- **Password Protection**: Salted PBKDF2-HMAC-SHA256 password hashing (240,000 iterations).
- **Session Management**: Secure HTTP-only cookies with SQL injection defense via parameterized queries.
- **Persistent Student Hub**: SQLite-backed user space preserving counselling histories, enrolled batches, and digital bursar receipts.

---

## Quick Start

### Prerequisites
- Python 3.10 or newer (no `pip install` required).

### Running Locally

1. Open a terminal in the `web-app` folder:

   ```powershell
   cd web-app
   ```

2. Start the local server:

   ```powershell
   python app.py
   ```

3. Open your browser at **[http://127.0.0.1:8000](http://127.0.0.1:8000)**.
4. Click **Create account** (or **Sign in**), then choose **Start counselling** to begin.

> **Port Configuration**: To run on a different port, set the `PORT` environment variable before starting:
> ```powershell
> $env:PORT="8080"; python app.py
> ```

To stop the server, press `Ctrl + C` in your terminal.

---

## Project Structure

```text
├── assets/                          # Portal screenshots and reference assets
│   ├── Screenshot 2026-11-19 234253.png
│   └── Screenshot 2026-11-20 000811.png
├── web-app/                         # Web application directory
│   ├── app.py                       # Python HTTP server, REST API, & recommendation engine
│   ├── app.js                       # Vanilla JavaScript state management & payment modal
│   ├── index.html                   # Semantic HTML5 accessible frontend
│   ├── style.css                    # Collegiate Oxford Navy & Gold responsive design system
│   ├── caats.sqlite3                # Local SQLite database (users, recommendations, enrollments)
│   └── SOURCE_RULES.md              # Detailed mapping of console source rules & boundaries
├── A_main.py                        # Original console authentication & flow coordinator
├── B_user_details.py                # Original console profession and age routing
├── C_school_dep.py                  # Original console school department
├── D_work_dep.py                    # Original console skills and master classes
├── E_clg_brch_choos.py              # Original console college course eligibility
├── F_Btech_clg_dep.py               # Original console B.Tech JEE percentile tables
├── G_Bsc_clg_dep.py                 # Original console B.Sc percentage tiers
├── I_Bca_clg_dep.py                 # Original console BCA percentage tiers
├── K_diploma_clg_dep.py             # Original console Diploma engineering rules
├── L_bat_prch.py                    # Original console course batch fee structures
└── README.md                        # Project documentation
```

---

## Design System

The portal adopts an academic collegiate identity:
- **Palette**: Deep Oxford Navy (`#0d233a`), Scholastic Slate Blue (`#184e77` / `#1e6091`), crisp background (`#fbfcfd`), and Warm Gold accents (`#c59247`).
- **Typography**: Modern serif headers paired with legible system sans-serif typography.
- **Accessibility**: Meets WCAG AA contrast standards, keyboard navigable forms, and full support for `prefers-reduced-motion`.

---

## Notes for Sharing and Deployment

This project is built for local learning, academic demonstration, and portfolio showcases:
- Sessions are stored in memory; local bindings attach to `127.0.0.1`.
- A production deployment should utilize HTTPS, persistent Redis or database-backed session stores, environment secrets, and a WSGI/ASGI application server behind Nginx or Caddy.
- The original console Python files remain completely untouched in the repository root.
