from pydantic import BaseModel


class TeamBase(BaseModel):
    name: str
    system_style: str


class TeamRead(TeamBase):
    id: int
    championships: int
    playoff_appearances: int
    legacy_score: float

    class Config:
        from_attributes = True


class PlayerCreate(BaseModel):
    name: str
    position: str
    age: int
    draft_year: int
    draft_pick: int
    draft_team_id: int | None = None
    college: str
    overall_rating: int
    top_attributes: str
    worst_attribute: str
    development_type: str
    prime_start_age: int
    prime_end_age: int
    personality_trait: str
    injury_risk: str
    speed: int
    shooting: int
    defense: int
    passing: int
    rebounding: int
    athleticism: int


class PlayerRead(BaseModel):
    id: int
    name: str
    position: str
    archetype: str
    overall_rating: int
    development_type: str

    class Config:
        from_attributes = True


class PlayerSeasonCreate(BaseModel):
    player_id: int
    season_year: int
    team_id: int
    games_played: int
    ppg: float
    rpg: float
    apg: float
    spg: float
    bpg: float
    overall_rating: int


class DraftOutcomeRequest(BaseModel):
    draft_pick: int
    career_ppg: float
    all_star_appearances: int = 0


class LegacyScoreRequest(BaseModel):
    championships: int = 0
    finals_mvps: int = 0
    mvps: int = 0
    all_nba: int = 0
    all_star: int = 0
    all_defense: int = 0
    all_rookie: int = 0
    dpoy: int = 0
    mip: int = 0
    seasons_25_ppg: int = 0
    seasons_20_ppg: int = 0
    seasons_double_double: int = 0
    seasons_10_reb: int = 0
    seasons_2_stl: int = 0
    seasons_2_blk: int = 0
    seasons_25_5_5: int = 0
