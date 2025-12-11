**Verdantia — Agent Instructions**

- **Repo Goals:** Build and maintain Verdantia, a text-based multiplayer RPG with a React TypeScript frontend and a Python FastAPI backend. Make the codebase extensible (data-driven skills, plugin registry), testable, and safe for contributors.

- **Where Code Lives:**
  - `frontend/` — React + TypeScript (strict) app
  - `backend/` — Python FastAPI app and domain code
  - `backend/migrations/` — Alembic migrations

- **Allowed Actions (Agent):**
  - Create and edit local files and branches.
  - Run local linters, formatters, and tests.
  - Create draft CI/workflow files **locally** (must not push or enable remotely).
  - Commit changes locally following branch/commit rules.

- **Forbidden Actions (Hard):**
  - No network pushes (no `git push`, no PR creation).
  - No network requests to external services except local dev servers.
  - Do not add repository secrets or modify remote settings.
  - Do not enable or trigger CI workflows on the remote repository.

- **Branching & Commits:**
  - Agent will create local branches named `agent/<task>-YYYYMMDD-<short>`.
  - Use Conventional Commits for commit messages (e.g., `feat(core): add Skill schema`).
  - Agent may amend or squash local commits while preparing patches.

- **Coding Conventions:**
  - Frontend: TypeScript (strict), React + Zustand, `eslint` + `prettier`.
  - Backend: Python 3.11+, FastAPI, `ruff` + `black`. Use `poetry` for dependency management.
  - Tests: `vitest` (frontend) and `pytest` (backend).

- **Run / Test Commands:**
  - Frontend:
    ```bash
    cd frontend
    pnpm install
    pnpm dev
    pnpm test
    ```
  - Backend:
    ```bash
    cd backend
    poetry install
    poetry run uvicorn verdantia.app:app --reload
    poetry run pytest
    ```

- **CI / Workflows:**
  - The agent may create workflow files locally for review but must not push or enable them.
  - All workflow changes require human review before being pushed.

- **Plugin / Skill Safety:**
  - Plugins and skill manifests must be data-driven and validated against a schema.
  - Adding a new plugin manifest requires a human approval step before enabling it in production/staging.

- **Escalation / Ask-Human Rules:**
  - If any change touches secrets, remote config, or CI triggers, stop and ask a human.
  - If a requested change requires network access (or credentials), stop and ask for explicit approval and credentials.

- **Change Log & Rollback:**
  - Record agent-made changes in `CHANGELOG.md` entries in commits or PR descriptions (human to push).
  - If rollback is needed, create a clear patch that a human can review and apply.

If you want the agent to operate under a different policy, edit this file and commit locally; human approval required before remote pushes.