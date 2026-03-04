-- Canonical PostgreSQL schema for NBA Legacy Universe Tracker
CREATE TABLE IF NOT EXISTS teams (
  id SERIAL PRIMARY KEY,
  name VARCHAR(120) UNIQUE NOT NULL,
  system_style VARCHAR(80) NOT NULL,
  championships INT DEFAULT 0,
  playoff_appearances INT DEFAULT 0,
  legacy_score INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS players (
  id SERIAL PRIMARY KEY,
  name VARCHAR(120) NOT NULL,
  position VARCHAR(20) NOT NULL,
  height VARCHAR(10) NOT NULL,
  weight INT NOT NULL,
  age INT NOT NULL,
  draft_year INT NOT NULL,
  draft_pick INT NOT NULL,
  draft_team_id INT REFERENCES teams(id),
  college VARCHAR(80),
  overall_rating INT NOT NULL,
  top_attributes VARCHAR(180) NOT NULL,
  worst_attribute VARCHAR(40) NOT NULL,
  archetype VARCHAR(80) NOT NULL,
  development_type VARCHAR(40) NOT NULL,
  prime_start_age INT NOT NULL,
  prime_end_age INT NOT NULL,
  personality_trait VARCHAR(40) NOT NULL,
  injury_risk VARCHAR(20) NOT NULL
);
