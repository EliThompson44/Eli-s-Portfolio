#!/usr/bin/env bash
set -euo pipefail
cat database/schema.sql | docker compose exec -T db psql -U legacy -d legacy_universe
cat database/seed.sql | docker compose exec -T db psql -U legacy -d legacy_universe
