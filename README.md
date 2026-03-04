# NBA Legacy Universe Tracker

NBA Legacy Universe Tracker is a full-stack web platform for preserving and analyzing an alternate NBA timeline starting in 1960 and extending indefinitely. It combines deep historical storage with automatic analytics such as legacy scoring, draft outcome classification, dynasty detection, rivalry tracking, and season storytelling.

## Stack

- **Frontend:** Next.js 14 + TypeScript + TailwindCSS
- **Backend:** FastAPI + SQLAlchemy + Pydantic
- **Database:** PostgreSQL 15
- **Infra:** Docker Compose + GitHub Actions CI

## Repository Layout

- `frontend/` — Next.js app (dashboard, players, timeline, comparisons)
- `backend/` — FastAPI service with models, APIs, and analytics engine
- `database/` — SQL schema and seed scripts
- `docs/` — architecture and module documentation
- `scripts/` — local automation helpers

## Quick Start

1. Copy environment variables:
   ```bash
   cp .env.example .env
   ```
2. Start all services:
   ```bash
   docker compose up --build
   ```
3. App URLs:
   - Frontend: http://localhost:3000
   - Backend API docs: http://localhost:8000/docs
   - PostgreSQL: localhost:5432

## Backend Development

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
uvicorn app.main:app --reload --port 8000
```

## Frontend Development

```bash
cd frontend
npm install
npm run dev
```

## Database Initialization

The backend auto-creates tables on startup. To initialize with SQL scripts:

```bash
psql "$DATABASE_URL" -f database/schema.sql
psql "$DATABASE_URL" -f database/seed.sql
```

## Core Modules Implemented

1. Franchise Dashboard
2. Player Database
3. Player Career Tracker
4. Draft Analyzer
5. Draft Outcome Detector
6. Trade Analyzer
7. Archetype Generator
8. Legacy Points Engine
9. Dynasty Tracker
10. Season Timeline Explorer
11. Franchise Hall of Fame
12. Rivalry Tracker
13. League Record Tracker
14. Player Comparison Tool
15. Season Story Engine

## Scale Targets

- 100+ seasons supported through indexed season/player tables
- 10,000+ players supported via normalized relational schema

## CI

GitHub Actions runs:
- backend unit tests
- Python lint checks
- frontend build

