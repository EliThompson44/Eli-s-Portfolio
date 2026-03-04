from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.entities import DraftProspect, Player, PlayerSeason, Season, Team, Trade
from app.schemas.common import (
    DraftOutcomeRequest,
    LegacyScoreRequest,
    PlayerCreate,
    PlayerRead,
    PlayerSeasonCreate,
    TeamBase,
    TeamRead,
)
from app.services.analytics import (
    classify_draft_outcome,
    classify_role,
    generate_archetype,
    legacy_points,
)

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/teams", response_model=TeamRead)
def create_team(payload: TeamBase, db: Session = Depends(get_db)) -> Team:
    team = Team(name=payload.name, system_style=payload.system_style)
    db.add(team)
    db.commit()
    db.refresh(team)
    return team


@router.get("/teams", response_model=list[TeamRead])
def list_teams(db: Session = Depends(get_db)) -> list[Team]:
    return db.query(Team).order_by(Team.name).all()


@router.post("/players", response_model=PlayerRead)
def create_player(payload: PlayerCreate, db: Session = Depends(get_db)) -> Player:
    archetype = generate_archetype(
        payload.speed,
        payload.shooting,
        payload.defense,
        payload.passing,
        payload.rebounding,
        payload.athleticism,
    )
    player = Player(
        name=payload.name,
        position=payload.position,
        age=payload.age,
        draft_year=payload.draft_year,
        draft_pick=payload.draft_pick,
        draft_team_id=payload.draft_team_id,
        college=payload.college,
        overall_rating=payload.overall_rating,
        top_attributes=payload.top_attributes,
        worst_attribute=payload.worst_attribute,
        archetype=archetype,
        development_type=payload.development_type,
        prime_start_age=payload.prime_start_age,
        prime_end_age=payload.prime_end_age,
        personality_trait=payload.personality_trait,
        injury_risk=payload.injury_risk,
    )
    db.add(player)
    db.commit()
    db.refresh(player)
    return player


@router.get("/players", response_model=list[PlayerRead])
def list_players(db: Session = Depends(get_db)) -> list[Player]:
    return db.query(Player).order_by(Player.name).all()


@router.post("/player-seasons")
def add_player_season(payload: PlayerSeasonCreate, db: Session = Depends(get_db)) -> dict[str, str]:
    season = PlayerSeason(**payload.model_dump())
    db.add(season)
    db.commit()
    return {"role": classify_role(payload.overall_rating)}


@router.post("/analytics/legacy-score")
def calculate_legacy_score(payload: LegacyScoreRequest) -> dict[str, int]:
    return {"legacy_score": legacy_points(payload.model_dump())}


@router.post("/analytics/draft-outcome")
def draft_outcome(payload: DraftOutcomeRequest) -> dict[str, str]:
    return {
        "classification": classify_draft_outcome(
            payload.draft_pick,
            payload.career_ppg,
            payload.all_star_appearances,
        )
    }


@router.get("/seasons/{year}")
def get_season(year: int, db: Session = Depends(get_db)) -> Season:
    season = db.query(Season).filter(Season.year == year).first()
    if not season:
        raise HTTPException(status_code=404, detail="Season not found")
    return season


@router.get("/trades")
def list_trades(db: Session = Depends(get_db)) -> list[Trade]:
    return db.query(Trade).order_by(Trade.season_year.desc()).all()


@router.get("/draft-prospects")
def list_draft_prospects(db: Session = Depends(get_db)) -> list[DraftProspect]:
    return db.query(DraftProspect).order_by(DraftProspect.draft_year.desc()).all()
