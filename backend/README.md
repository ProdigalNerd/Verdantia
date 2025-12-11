Backend (FastAPI) for Verdantia

Quick start (local dev):

```bash
cd backend
poetry install
poetry shell
poetry run uvicorn verdantia.app:app --reload
```

Migrations:
- Alembic is used for Postgres migrations. Migration scripts live in `backend/migrations/`.
- For local prototyping you can use SQLite and the same Alembic scripts with a local DB URL.

Testing:

```bash
poetry run pytest
```
