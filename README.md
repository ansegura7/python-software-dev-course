# Python Software Development Course :snake:

This repository contains resources, examples, and exercises for the **Python Software Development Course**. The program is a condensed **8-session (16-hour)**, hands-on journey for beginners to build real skills and a starter portfolio.

## What You Will Learn (8 Sessions)

1) **Software Architecture + Employability I**  
   Frontend, backend, databases, APIs and real-world roles. Market overview, portfolio mindset.

2) **Python I + VS Code + Git**  
   Python syntax, variables, types, conditionals. Environment setup, Git basics.

3) **Python II + Data Structures + Functions (+ Jupyter optional)**  
   Lists, dicts, loops, functions, problem-solving practice.

4) **Python III + Files + GitHub + Local Project**  
   Reading/writing files (CSV/JSON), small CRUD, pushing code to GitHub.

5) **Databases (SQLite) + SQL + Tools**  
   SQLite basics, schema, CRUD with SQL, DB Browser/SQLite Viewer.

6) **Backend with FastAPI + REST**  
   Minimal REST API (GET/POST), validation, testing with Swagger/Postman. SQLite integration.

7) **Frontend: HTML, CSS, JS + API Integration**  
   Simple UI, forms, `fetch()` to call FastAPI, display responses.

8) **Final Project + Employability II**  
   Integrate frontend + backend + DB. Demo day, GitHub portfolio checklist, LinkedIn polish.

## Repository Structure

- `notebooks/` → Jupyter notebooks for in-class practice.  
- `examples/` → Small, focused code examples (Python basics, SQL snippets, JS fetch samples).  
- `apps/` → Mini projects / demo apps:
  - `survey-dashboard/` (Dash app for the class survey)
  - `fastapi-demo/` (minimal REST API)
  - `fullstack-example/` (front + API + DB, final integration)
<!-- - `api/` → FastAPI service(s) if you prefer to keep them outside `apps/`.
- `frontend/` → HTML/CSS/JS assets if you keep the UI separate from `apps/`. -->
- `data/` → Sample datasets (CSV/JSON) used in notebooks and apps.
- `resources/` → Course materials: **course presentation**, **syllabus PDF**, handouts, checklists.
- `exercises/` → Practice assignments per session.
<!-- - `solutions/` → Suggested solutions (optional; consider keeping it private). -->

## Getting Started

```bash
> git clone https://github.com/ansegura7/python-software-dev-course.git
> cd python-software-dev-course

# (optional) create a virtual environment
> python -m venv .venv
> .venv/bin/activate  # Windows: .venv\Scripts\activate

# update pip
> python.exe -m pip install --upgrade pip

# install common tools
> pip install -r requirements.txt
```

## License

This project is licensed under the terms of the MIT license.
