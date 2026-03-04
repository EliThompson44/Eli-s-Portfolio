from __future__ import annotations

from datetime import date
from sqlalchemy import Date, Float, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Team(Base):
    __tablename__ = "teams"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), unique=True)
    system_style: Mapped[str] = mapped_column(String(80))
    championships: Mapped[int] = mapped_column(Integer, default=0)
    playoff_appearances: Mapped[int] = mapped_column(Integer, default=0)
    legacy_score: Mapped[int] = mapped_column(Integer, default=0)


class Player(Base):
    __tablename__ = "players"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), index=True)
    position: Mapped[str] = mapped_column(String(20))
    height: Mapped[str] = mapped_column(String(10))
    weight: Mapped[int] = mapped_column(Integer)
    age: Mapped[int] = mapped_column(Integer)
    draft_year: Mapped[int] = mapped_column(Integer)
    draft_pick: Mapped[int] = mapped_column(Integer)
    draft_team_id: Mapped[int | None] = mapped_column(ForeignKey("teams.id"), nullable=True)
    college: Mapped[str | None] = mapped_column(String(80), nullable=True)
    overall_rating: Mapped[int] = mapped_column(Integer)
    top_attributes: Mapped[str] = mapped_column(String(180))
    worst_attribute: Mapped[str] = mapped_column(String(40))
    archetype: Mapped[str] = mapped_column(String(80))
    development_type: Mapped[str] = mapped_column(String(40))
    prime_start_age: Mapped[int] = mapped_column(Integer)
    prime_end_age: Mapped[int] = mapped_column(Integer)
    personality_trait: Mapped[str] = mapped_column(String(40))
    injury_risk: Mapped[str] = mapped_column(String(20))

    seasons: Mapped[list[PlayerSeason]] = relationship(back_populates="player", cascade="all, delete-orphan")


class PlayerSeason(Base):
    __tablename__ = "player_seasons"
    __table_args__ = (UniqueConstraint("player_id", "season_year", name="uq_player_season"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    player_id: Mapped[int] = mapped_column(ForeignKey("players.id", ondelete="CASCADE"))
    season_year: Mapped[int] = mapped_column(Integer, index=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    games_played: Mapped[int] = mapped_column(Integer)
    ppg: Mapped[float] = mapped_column(Float)
    rpg: Mapped[float] = mapped_column(Float)
    apg: Mapped[float] = mapped_column(Float)
    spg: Mapped[float] = mapped_column(Float)
    bpg: Mapped[float] = mapped_column(Float)
    overall_rating: Mapped[int] = mapped_column(Integer)
    role_classification: Mapped[str] = mapped_column(String(50))

    player: Mapped[Player] = relationship(back_populates="seasons")


class Season(Base):
    __tablename__ = "seasons"

    id: Mapped[int] = mapped_column(primary_key=True)
    year: Mapped[int] = mapped_column(Integer, unique=True)
    champion_team_id: Mapped[int | None] = mapped_column(ForeignKey("teams.id"), nullable=True)
    finals_matchup: Mapped[str | None] = mapped_column(String(120), nullable=True)
    league_mvp_player_id: Mapped[int | None] = mapped_column(ForeignKey("players.id"), nullable=True)
    standings_json: Mapped[str | None] = mapped_column(Text, nullable=True)
    draft_class_summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    major_trades: Mapped[str | None] = mapped_column(Text, nullable=True)
    key_storyline_1: Mapped[str | None] = mapped_column(Text, nullable=True)
    key_storyline_2: Mapped[str | None] = mapped_column(Text, nullable=True)


class AwardRecord(Base):
    __tablename__ = "award_records"

    id: Mapped[int] = mapped_column(primary_key=True)
    player_id: Mapped[int] = mapped_column(ForeignKey("players.id", ondelete="CASCADE"))
    season_year: Mapped[int] = mapped_column(Integer)
    award_type: Mapped[str] = mapped_column(String(30))


class Trade(Base):
    __tablename__ = "trades"

    id: Mapped[int] = mapped_column(primary_key=True)
    trade_date: Mapped[date] = mapped_column(Date)
    season_year: Mapped[int] = mapped_column(Integer)
    team_a_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    team_b_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    team_a_assets: Mapped[str] = mapped_column(Text)
    team_b_assets: Mapped[str] = mapped_column(Text)
    evaluation_grade: Mapped[str | None] = mapped_column(String(2), nullable=True)


class DraftProspect(Base):
    __tablename__ = "draft_prospects"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    draft_year: Mapped[int] = mapped_column(Integer, index=True)
    college_ppg: Mapped[float] = mapped_column(Float)
    college_rpg: Mapped[float] = mapped_column(Float)
    college_apg: Mapped[float] = mapped_column(Float)
    fg_pct: Mapped[float] = mapped_column(Float)
    notable_teammates: Mapped[str | None] = mapped_column(Text, nullable=True)
    strengths: Mapped[str | None] = mapped_column(Text, nullable=True)
    weaknesses: Mapped[str | None] = mapped_column(Text, nullable=True)
    projected_ceiling: Mapped[str | None] = mapped_column(String(50), nullable=True)
    projected_floor: Mapped[str | None] = mapped_column(String(50), nullable=True)
    expected_tier: Mapped[str | None] = mapped_column(String(30), nullable=True)


class Dynasty(Base):
    __tablename__ = "dynasties"

    id: Mapped[int] = mapped_column(primary_key=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    start_year: Mapped[int] = mapped_column(Integer)
    end_year: Mapped[int] = mapped_column(Integer)
    championships_won: Mapped[int] = mapped_column(Integer)


class Rivalry(Base):
    __tablename__ = "rivalries"

    id: Mapped[int] = mapped_column(primary_key=True)
    team_a_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    team_b_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    playoff_meetings: Mapped[int] = mapped_column(Integer, default=0)
    series_record: Mapped[str | None] = mapped_column(String(20), nullable=True)
    notable_games: Mapped[str | None] = mapped_column(Text, nullable=True)


class FranchiseHallOfFame(Base):
    __tablename__ = "franchise_hof"

    id: Mapped[int] = mapped_column(primary_key=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.id"))
    player_id: Mapped[int] = mapped_column(ForeignKey("players.id"))
    reason: Mapped[str] = mapped_column(String(180))


class LeagueRecord(Base):
    __tablename__ = "league_records"

    id: Mapped[int] = mapped_column(primary_key=True)
    record_key: Mapped[str] = mapped_column(String(80), unique=True)
    holder_player_id: Mapped[int | None] = mapped_column(ForeignKey("players.id"), nullable=True)
    holder_team_id: Mapped[int | None] = mapped_column(ForeignKey("teams.id"), nullable=True)
    value: Mapped[float] = mapped_column(Float)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
