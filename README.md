# Task Manager API

A small REST API for managing tasks, built with FastAPI.

## What this project does

The API supports:

- Creating tasks
- Listing tasks
- Completing tasks
- Deleting tasks
- Health checks

The application is intentionally small while still separating HTTP handling, business logic, persistence, and validation.

## Architecture

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

Create a virtual environment:

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

## Run tests

```bash
pytest
```

## API endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /health | Health check |
| POST | /tasks | Create a task |
| GET | /tasks | List tasks |
| PATCH | /tasks/{task_id}/complete | Mark a task as completed |
| DELETE | /tasks/{task_id} | Delete a task |

## Notes

Task data is currently stored in memory, so it is lost when the application restarts.

This repository is intentionally small and suitable for experimenting with API design, testing, architecture, and developer tooling.
