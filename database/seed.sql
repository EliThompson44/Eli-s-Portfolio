INSERT INTO teams (name, system_style, championships, playoff_appearances, legacy_score)
VALUES
('Chicago Zephyrs', 'Triangle Offense', 3, 20, 870),
('Seattle Meteors', 'Run and Gun', 1, 15, 610)
ON CONFLICT DO NOTHING;

INSERT INTO players (
  name, position, height, weight, age, draft_year, draft_pick, draft_team_id, college,
  overall_rating, top_attributes, worst_attribute, archetype, development_type,
  prime_start_age, prime_end_age, personality_trait, injury_risk
)
VALUES (
  'Marcus Hale', 'SG', '6-6', 210, 24, 1964, 5, 1, 'UCLA', 88,
  'shooting,defense,athleticism', 'rebounding', 'Two Way Slashing Wing', 'Linear Growth',
  24, 31, 'Leader', 'Durable'
)
ON CONFLICT DO NOTHING;
