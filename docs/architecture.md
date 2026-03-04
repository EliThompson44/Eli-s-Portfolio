# NBA Legacy Universe Tracker - System Architecture

## Overview

The system stores a permanent alternate NBA history from 1960 onward with season permanence, player career narratives, and automated analytics. It is separated into:

- Next.js frontend for dashboards, exploration, and data entry UX.
- FastAPI backend for REST endpoints and analytics engines.
- PostgreSQL for normalized historical storage.

## Data Model Highlights

- `teams`: team metadata, tactical system style, franchise-level success metrics.
- `players`: static biographical, draft, archetype, and development profile data.
- `player_seasons`: year-by-year production, team, and progression snapshots.
- `seasons`: champion, finals matchup, MVP, standings snapshot, storylines.
- `trades`: exchanged assets and retrospective grade.
- `draft_prospects`: pre-draft profile, teammate context, projections.

## Analytics Modules

- Archetype Generator from six core attributes.
- Role Classification using overall rating tiers.
- Draft Outcome Detector based on pick context + realized value.
- Legacy Points Engine with weighted achievements + stat bonuses.
- Dynasty Detector (3 titles in 5-season window).
- Hall of Fame qualification helpers.
- Trade analyzer grade helper.

## Scalability

The relational schema supports 10,000+ players and 100+ seasons using:

- indexes on player name and player-season composite keys,
- normalized season rows,
- API pagination extension points.
