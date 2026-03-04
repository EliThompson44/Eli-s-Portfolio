# NBA Legacy Universe Tracker - Architecture

## Overview
- **Frontend:** Next.js 14 + TypeScript + TailwindCSS.
- **Backend:** FastAPI + SQLAlchemy.
- **Database:** PostgreSQL with bootstrap SQL scripts.
- **Deployment:** Docker Compose for local dev, GitHub Actions for CI.

## Core Modules Implemented
1. Franchise Dashboard
2. Player Database
3. Player Career Tracker
4. Draft Analyzer
5. Draft Outcome Detector
6. Trade Analyzer
7. Archetype Generator (model field + API ready)
8. Legacy Points Engine
9. Dynasty Tracker
10. Season Timeline Explorer
11. Franchise Hall of Fame (schema)
12. Rivalry Tracker (schema)
13. League Record Tracker (schema)
14. Player Comparison Tool
15. Season Story Engine

## Scale Notes
- Postgres-backed normalized schema supports 10,000+ players and 100+ seasons.
- Indexed fields: player names, season years, draft years.
