Alembic migrations for Verdantia

This directory will contain Alembic configuration and migration scripts.

Local development: you can use SQLite for convenience; for staging/production use Postgres.

Example Alembic usage (after installing dependencies):

```bash
cd backend
poetry run alembic revision --autogenerate -m "create players"
poetry run alembic upgrade head
```
