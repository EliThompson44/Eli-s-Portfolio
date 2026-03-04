# NBA Legacy Universe Tracker

Production-ready monorepo for tracking an alternate NBA universe from 1960 onward.

## Stack
- **Frontend:** Next.js + TypeScript + TailwindCSS
- **Backend:** FastAPI + SQLAlchemy
- **Database:** PostgreSQL
- **Infra:** Docker + GitHub Actions

## Repository Layout
- `frontend/` Next.js web app
- `backend/` FastAPI services and analytics engine
- `database/` SQL schema and seed scripts
- `docs/` architecture and API documentation
- `scripts/` local helper scripts

## Features
- Franchise dashboard with team system style, championships, playoff appearances, legacy score.
- Player database with full profile fields, development type, personality, injury risk.
- Player season tracking and role tier classification.
- Draft analyzer with projected tier/strengths/weaknesses.
- Draft outcome classification + late bloomer detection (service logic).
- Trade analyzer with grade output.
- Legacy points engine.
- Dynasty detector (3 titles in 5 seasons).
- Timeline explorer and storyline logging fields.
- Player comparison endpoint by legacy score.

## Quick Start (Docker)
1. Copy env file:
   ```bash
   cp .env.example .env
   ```
2. Start all services:
   ```bash
   docker compose up --build
   ```
3. Visit:
   - Frontend: http://localhost:3000
   - Backend docs: http://localhost:8000/docs

## Local Development (without Docker)
### Backend
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Database Initialization
Use Docker database service and run:
```bash
./scripts/init-db.sh
```

## Data Capacity Guidance
- Designed for 100+ seasons and 10,000+ players.
- Use Postgres indexes and add partitioning for `player_seasons` when scaling beyond initial target.

## CI
GitHub Actions workflow (`.github/workflows/ci.yml`) runs:
- backend dependency install + import check
- frontend dependency install + build

## Future Extensions
- Auth and multi-save universes.
- Advanced visual analytics (Recharts pages).
- Automated rivalry and hall-of-fame materialized views.
