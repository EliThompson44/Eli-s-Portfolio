INSERT INTO teams (name, system_style, championships, playoff_appearances, legacy_score)
VALUES
  ('Chicago Steel', 'Triangle Offense', 6, 19, 1210),
  ('Seattle Emeralds', 'Seven Seconds or Less', 4, 12, 872)
ON CONFLICT (name) DO NOTHING;
