# CAATS University counselling website

A beginner-friendly full-stack version of the CAATS University console project. It uses Python’s built-in web server, a small JSON API, plain HTML/CSS/JavaScript, and SQLite. No package installation is required.

## Run it

1. Install Python 3.10 or newer.
2. Open a terminal in this `web-app` folder.
3. Run:

   ```powershell
   python app.py
   ```

4. Open [http://127.0.0.1:8000](http://127.0.0.1:8000).
5. Create an account, then use **Start counselling**. Your account, profile, and saved results are stored in `caats.sqlite3` next to `app.py`.

Stop the local server with `Ctrl+C`. To use another local port, set the `PORT` environment variable before running the app.

## What is included

- Responsive home page and guided counselling flow.
- Registration and login with salted password hashing.
- Session cookie and profile persistence.
- Student, working, and other pathways; school, college, skills, and four-hour master class choices.
- BSc, BCA, and BTech recommendations mapped from the uploaded source.
- Saved recommendations and profile shown in the student space.
- SQLite schema created automatically at first run.

See [SOURCE_RULES.md](SOURCE_RULES.md) for a feature map and the source inconsistencies that need a project decision.

## Before sharing or deploying

This is designed for local learning and a GitHub project demo. The session store is in memory, the local server binds only to `127.0.0.1`, and the app does not include production hosting protections. Do not put real student records or real passwords into a public deployment. A hosted version should use HTTPS, persistent session storage, environment-based secrets, backups, and a production-ready server. SQLite is a good starting database; PostgreSQL can be considered when the project needs a hosted multi-user database.

The SQLite database is local user data and is excluded from Git. The original uploaded Python files are not moved, overwritten, or deleted by this website.
