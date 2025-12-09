# Core service (minimal)

This repository contains a minimal `Core` microservice scaffold (FastAPI) that demonstrates MySQL database access and Alembic migrations.

Quick start (development):

1. Install dependencies (using Poetry):

```powershell
poetry install
poetry shell
```

2. Set environment variables (see `.env.example`):

```powershell
copy .env.example .env
# Edit .env to set your MySQL connection
```

3. Apply migrations (Alembic):

```powershell
alembic upgrade head
```

4. Run the app:

```powershell
uvicorn core.main:app --reload
```

Notes
- Database URL is read from `DATABASE_URL` env var.
- Alembic configuration is in `alembic.ini` and `alembic/env.py`.
