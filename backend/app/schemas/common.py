from datetime import date
from pydantic import BaseModel, Field


class TeamBase(BaseModel):
    name: str
    system_style: str
    championships: int = 0
    playoff_appearances: int = 0
    legacy_score: int = 0


class TeamRead(TeamBase):
    id: int

    class Config:
        from_attributes = True


class PlayerBase(BaseModel):
    name: str
    position: str
    height: str
    weight: int
    age: int
    draft_year: int
    draft_pick: int
    draft_team_id: int | None = None
    college: str | None = None
    overall_rating: int
    top_attributes: str
    worst_attribute: str
    archetype: str
    development_type: str
    prime_start_age: int
    prime_end_age: int
    personality_trait: str
    injury_risk: str


class PlayerRead(PlayerBase):
    id: int

    class Config:
        from_attributes = True


class PlayerSeasonBase(BaseModel):
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
    role_classification: str | None = Field(default=None)


class PlayerSeasonRead(PlayerSeasonBase):
    id: int

    class Config:
        from_attributes = True


class SeasonBase(BaseModel):
    year: int
    champion_team_id: int | None = None
    finals_matchup: str | None = None
    league_mvp_player_id: int | None = None
    standings_json: str | None = None
    draft_class_summary: str | None = None
    major_trades: str | None = None
    key_storyline_1: str | None = None
    key_storyline_2: str | None = None


class SeasonRead(SeasonBase):
    id: int

    class Config:
        from_attributes = True


class TradeBase(BaseModel):
    trade_date: date
    season_year: int
    team_a_id: int
    team_b_id: int
    team_a_assets: str
    team_b_assets: str


class TradeRead(TradeBase):
    id: int
    evaluation_grade: str | None = None

    class Config:
        from_attributes = True


class DraftProspectBase(BaseModel):
    name: str
    draft_year: int
    college_ppg: float
    college_rpg: float
    college_apg: float
    fg_pct: float
    notable_teammates: str | None = None


class DraftProspectRead(DraftProspectBase):
    id: int
    strengths: str | None = None
    weaknesses: str | None = None
    projected_ceiling: str | None = None
    projected_floor: str | None = None
    expected_tier: str | None = None

    class Config:
        from_attributes = True


class PlayerComparisonResponse(BaseModel):
    player_a: PlayerRead
    player_b: PlayerRead
    legacy_a: int
    legacy_b: int
    verdict: str
