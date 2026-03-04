CREATE TABLE IF NOT EXISTS teams (
  id SERIAL PRIMARY KEY,
  name VARCHAR(120) UNIQUE NOT NULL,
  system_style VARCHAR(60) NOT NULL,
  championships INTEGER DEFAULT 0,
  playoff_appearances INTEGER DEFAULT 0,
  legacy_score NUMERIC(10,2) DEFAULT 0
);

CREATE TABLE IF NOT EXISTS players (
  id SERIAL PRIMARY KEY,
  name VARCHAR(120) NOT NULL,
  position VARCHAR(5) NOT NULL,
  age INTEGER NOT NULL,
  draft_year INTEGER NOT NULL,
  draft_pick INTEGER NOT NULL,
  draft_team_id INTEGER REFERENCES teams(id),
  college VARCHAR(120) NOT NULL,
  overall_rating INTEGER NOT NULL,
  top_attributes VARCHAR(120) NOT NULL,
  worst_attribute VARCHAR(40) NOT NULL,
  archetype VARCHAR(120) NOT NULL,
  development_type VARCHAR(40) NOT NULL,
  prime_start_age INTEGER NOT NULL,
  prime_end_age INTEGER NOT NULL,
  personality_trait VARCHAR(40) NOT NULL,
  injury_risk VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS player_seasons (
  id SERIAL PRIMARY KEY,
  player_id INTEGER NOT NULL REFERENCES players(id),
  season_year INTEGER NOT NULL,
  team_id INTEGER NOT NULL REFERENCES teams(id),
  games_played INTEGER NOT NULL,
  ppg NUMERIC(5,2) NOT NULL,
  rpg NUMERIC(5,2) NOT NULL,
  apg NUMERIC(5,2) NOT NULL,
  spg NUMERIC(4,2) NOT NULL,
  bpg NUMERIC(4,2) NOT NULL,
  overall_rating INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_players_name ON players(name);
CREATE INDEX IF NOT EXISTS idx_player_seasons_player_year ON player_seasons(player_id, season_year);
