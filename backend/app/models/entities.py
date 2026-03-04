from sqlalchemy import Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True)
    system_style: Mapped[str] = mapped_column(String(60))
    championships: Mapped[int] = mapped_column(Integer, default=0)
    playoff_appearances: Mapped[int] = mapped_column(Integer, default=0)
    legacy_score: Mapped[float] = mapped_column(Float, default=0)


class Player(Base):
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), index=True)
    position: Mapped[str] = mapped_column(String(5))
    age: Mapped[int] = mapped_column(Integer)
    draft_year: Mapped[int] = mapped_column(Integer)
    draft_pick: Mapped[int] = mapped_column(Integer)
    draft_team_id: Mapped[int | None] = mapped_column(ForeignKey("teams.id"), nullable=True)
    college: Mapped[str] = mapped_column(String(120))
    overall_rating: Mapped[int] = mapped_column(Integer)
    top_attributes: Mapped[str] = mapped_column(String(120))
    worst_attribute: Mapped[str] = mapped_column(String(40))
    archetype: Mapped[str] = mapped_column(String(120))
    development_type: Mapped[str] = mapped_column(String(40))
    prime_start_age: Mapped[int] = mapped_column(Integer)
    prime_end_age: Mapped[int] = mapped_column(Integer)
    personality_trait: Mapped[str] = mapped_column(String(40))
    injury_risk: Mapped[str] = mapped_column(String(20))

    seasons: Mapped[list["PlayerSeason"]] = relationship(back_populates="player")


class PlayerSeason(Base):
    __tablename__ = "player_seasons"

    id: Mapped[int] = mapped_column(primary_key=True)
    player_id: Mapped[int] = mapped_column(ForeignKey("players.id"), index=True)
    season_year: Mapped[int] = mapped_column(Integer, index=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    games_played: Mapped[int] = mapped_column(Integer)
    ppg: Mapped[float] = mapped_column(Float)
    rpg: Mapped[float] = mapped_column(Float)
    apg: Mapped[float] = mapped_column(Float)
    spg: Mapped[float] = mapped_column(Float)
    bpg: Mapped[float] = mapped_column(Float)
    overall_rating: Mapped[int] = mapped_column(Integer)

    player: Mapped[Player] = relationship(back_populates="seasons")


class Season(Base):
    __tablename__ = "seasons"

    id: Mapped[int] = mapped_column(primary_key=True)
    year: Mapped[int] = mapped_column(Integer, unique=True)
    champion_team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    finals_matchup: Mapped[str] = mapped_column(String(120))
    mvp_player_id: Mapped[int | None] = mapped_column(ForeignKey("players.id"), nullable=True)
    standings_snapshot: Mapped[str] = mapped_column(Text)
    draft_class_summary: Mapped[str] = mapped_column(Text)
    major_trades_summary: Mapped[str] = mapped_column(Text)
    key_storyline_1: Mapped[str] = mapped_column(Text)
    key_storyline_2: Mapped[str] = mapped_column(Text)


class Trade(Base):
    __tablename__ = "trades"

    id: Mapped[int] = mapped_column(primary_key=True)
    season_year: Mapped[int] = mapped_column(Integer, index=True)
    team_a_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    team_b_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    assets_a: Mapped[str] = mapped_column(Text)
    assets_b: Mapped[str] = mapped_column(Text)
    evaluation_grade: Mapped[str] = mapped_column(String(2), default="C")


class DraftProspect(Base):
    __tablename__ = "draft_prospects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), index=True)
    draft_year: Mapped[int] = mapped_column(Integer, index=True)
    college_ppg: Mapped[float] = mapped_column(Float)
    college_rpg: Mapped[float] = mapped_column(Float)
    college_apg: Mapped[float] = mapped_column(Float)
    fg_pct: Mapped[float] = mapped_column(Float)
    notable_teammates: Mapped[str] = mapped_column(Text)
    strengths: Mapped[str] = mapped_column(Text)
    weaknesses: Mapped[str] = mapped_column(Text)
    projected_ceiling: Mapped[str] = mapped_column(String(120))
    projected_floor: Mapped[str] = mapped_column(String(120))
    expected_tier: Mapped[str] = mapped_column(String(30))
