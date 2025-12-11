Plan: Monorepo scaffold for Verdantia

TL;DR: Create a two-app monorepo with `frontend/` (React + TypeScript strict, Vite, `pnpm`, `zustand`, `vitest`, `eslint`+`prettier`) and `backend/` (FastAPI + `uvicorn`, `poetry`, Postgres + Alembic migrations, `pytest`, `ruff`+`black`). Add a clear domain model (`Game`, `Entity`, `Skill`), a plugin/skill registry, a stable WebSocket protocol, workspace scripts, CI skeleton, and an `AGENT.md` that allows local commits but forbids network pushes and external requests. This makes the project extensible, testable, and safe for an automated agent to work locally.

Steps
1. Create top-level layout: add `AGENT.md`, `README.md`, `pnpm-workspace.yaml`, and root `package.json`.
2. Scaffold frontend: add `frontend/package.json`, `frontend/tsconfig.json` (strict), `frontend/vite.config.ts`, `frontend/src/` (`App.tsx`, `src/state/useGameStore.ts`), and `frontend/test/` (vitest).
3. Scaffold backend: add `backend/pyproject.toml` (poetry), `backend/verdantia/` with `core` (`Game`, `Entity`, `Skill`), `plugins` (`PluginManager`), `storage` (adapter interfaces), and `ws_protocol` message types.
4. Persistence & migrations: add Postgres adapter and Alembic scaffold under `backend/migrations/`, plus `backend/docs/migrations.md`.
5. Tooling & checks: add `frontend/.eslintrc.cjs`, `frontend/.prettierrc`, `backend/pyproject.toml` settings for `ruff` + `black`, and CI skeleton `.github/workflows/ci.yml` (local-draft only).
6. Tests, docs, agent rules: add `frontend/test/` (vitest), `backend/tests/` (pytest), `backend/docs/domain.md`, and finalize `AGENT.md` with branch/commit policy (`agent/<task>-YYYYMMDD-<short>`, Conventional Commits).

Further Considerations
1. Branch policy: agent creates local branches `agent/<task>-YYYYMMDD-<short>`; human pushes.
2. Commit conventions: recommend Conventional Commits for clear history and automated changelogs.
3. Secrets: require human-managed `.env` and never store secrets in repo or agent-added files.

Extensibility & Architecture Guidance
- Domain model: design `Game`, `Entity`, and `Skill` as explicit typed models in `backend/verdantia/core/` with stable interfaces.
- Plugin/Skill system: implement a `PluginManager` + registry under `backend/verdantia/plugins/`. Plugins should be declarative (manifest + handlers) and follow a sandbox/validation lifecycle (manifest validation, signature/approval, human enable step).
- Data-driven skills: store skills as JSON or YAML manifests (`backend/verdantia/skills/`), with a clear schema (name, id, cost, effects, triggers, cooldown, tags, metadata). Keep logic in handlers rather than in data when possible.
- Storage adapter: create adapter pattern in `backend/verdantia/storage/` to switch between SQLite (local dev) and Postgres (staging/prod). Provide migrations via Alembic and store migration scripts in `backend/migrations/`.
- WebSocket protocol: define a small message schema and versioning in `backend/verdantia/ws_protocol.py` and mirror types in `frontend/src/ws/protocol.ts`. Use message envelopes: `{"v":1, "type":"eventName", "id":"uuid", "payload":{}}`.
- Frontend architecture: organize `frontend/src/features/*` with isolated state slices in `zustand` (`useGameStore`) and components under `components/`. Keep business logic in small modules and state shape stable to make upgrades safe.

Tooling & Defaults
- Frontend: `pnpm` + `vite` + React + TypeScript (strict). Tests: `vitest`. Lint & format: `eslint` + `prettier` with recommended configs for React + TS.
- Backend: `poetry` for dependency management, `FastAPI` + `uvicorn` for WebSockets and HTTP, `pytest` for tests. Linting & formatting: `ruff` + `black`.
- CI: Draft GitHub Actions in `.github/workflows/ci.yml` that run `pnpm install && pnpm test` for frontend and `poetry install && pytest` for backend. Agent may create workflow files locally but must not push or enable them.

Agent Safety Rules (to be included in `AGENT.md`)
- Allowed: create files, create local commits, run local linters/tests, generate patches and branch locally.
- Forbidden: pushing branches, creating/updating remote refs, sending network requests (except local-only dev servers), writing secrets, enabling CI workflows or adding repository secrets, and modifying `.git/config` or `.github/` settings that require remote activation without human approval.
- Review/Enable: any change that creates or modifies a workflow, new external dependency, or plugin manifest must be flagged and require explicit human approval before push.
- Branch naming & commits: agent will create branches named `agent/<task>-YYYYMMDD-<short>`. Commits use Conventional Commits; the agent may format and lint changes before committing.

Next steps (after you review this plan file)
- Approve the plan or request edits.
- Once approved, the agent will scaffold files and run local tests/linting; all changes will be created in a local branch for your review.

Commands (local developer quick-start)

Activate Python dev environment (poetry):

```bash
cd backend
poetry install
poetry shell
uvicorn verdantia.app:app --reload
```

Frontend quick-start (pnpm):

```bash
cd frontend
pnpm install
pnpm dev
```

Run all tests locally from repo root (when dependencies installed):

```bash
# frontend
cd frontend && pnpm test
# backend
cd backend && poetry run pytest
```

Migration notes
- Use Alembic in `backend/migrations/` for Postgres migrations. Local dev may use SQLite adapter and the same Alembic scripts with environment-specific DB URLs.

Open questions for finalization
- Confirm Conventional Commits (accepted?), automatic local branch creation by the agent (accepted?), and plugin activation policy (human-approval required).

Status
- All high-level decisions confirmed by the user: TypeScript strict, pnpm, poetry, FastAPI + uvicorn, vitest + pytest, eslint+prettier, ruff+black, Postgres migrations, data-driven skills, sandbox policy accepted.


