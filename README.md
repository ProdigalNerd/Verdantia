Verdantia

Monorepo for a text-based RPG.

Structure
- `frontend/` — React + TypeScript client (Vite, pnpm)
- `backend/` — FastAPI server (Poetry, Alembic migrations)

Quick start

Frontend:

```bash
cd frontend
pnpm install
pnpm dev
```

Backend (Poetry):

```bash
cd backend
poetry install
poetry run uvicorn verdantia.app:app --reload
```

Agent policy in `AGENT.md` — the agent may create local commits/branches but must not push or enable CI workflows.