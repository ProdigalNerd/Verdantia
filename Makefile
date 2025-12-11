# Simple Makefile for common tasks
.PHONY: start-frontend start-backend test

start-frontend:
	cd frontend && pnpm install && pnpm dev

start-backend:
	cd backend && poetry install && poetry run uvicorn verdantia.app:app --reload

test-frontend:
	cd frontend && pnpm test

test-backend:
	cd backend && poetry run pytest

test: test-frontend test-backend
