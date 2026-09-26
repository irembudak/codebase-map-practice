# Codebase Map Practice

A small Task Manager API designed specifically for practicing the `rdilruba/codebase-map` skill.

## What this project does

It exposes a REST API for creating, listing, completing, and deleting tasks.

The project is intentionally small, but it has multiple layers:

```text
HTTP Request
    ↓
API Route
    ↓
Task Service
    ↓
Task Repository
    ↓
In-memory data store
```

## Project structure

```text
app/
├── __init__.py
├── main.py
├── api/
│   ├── __init__.py
│   └── routes.py
├── models/
│   ├── __init__.py
│   └── task.py
├── repositories/
│   ├── __init__.py
│   └── task_repository.py
├── services/
│   ├── __init__.py
│   └── task_service.py
└── utils/
    ├── __init__.py
    └── validation.py

tests/
├── __init__.py
└── test_tasks.py

requirements.txt
```

## Run locally

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the API:

```bash
uvicorn app.main:app --reload
```

Then open:

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs

Run tests:

```bash
pytest
```

## Your codebase-map exercise

Do **not** read every source file immediately.

First run the codebase-map skill against this repository.

Then answer these questions from the generated map:

1. Where is the application entry point?
2. What happens when `POST /tasks` is called?
3. Where is the business logic?
4. Where is task data stored?
5. Which modules depend on `TaskRepository`?
6. What is the simplest path from an HTTP request to stored data?
7. Which files would you change to add task filtering?
8. What assumptions or unknowns should you verify by running the application?

### First implementation task

After mapping the repository, implement:

```text
GET /tasks/{task_id}
```

Do it yourself first. Use the map to decide which files need to change.

Do not ask an AI to implement it immediately. The purpose of this repository is to practice navigating an unfamiliar codebase.
