from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.entities import DraftProspect, Player, PlayerSeason, Season, Team, Trade
from app.schemas.common import (
    DraftProspectBase,
    DraftProspectRead,
    PlayerBase,
    PlayerComparisonResponse,
    PlayerRead,
    PlayerSeasonBase,
    PlayerSeasonRead,
    SeasonBase,
    SeasonRead,
    TeamBase,
    TeamRead,
    TradeBase,
    TradeRead,
)
from app.services.analytics import (
    analyze_draft_tier,
    classify_draft_outcome,
    classify_role,
    compute_legacy_score,
    detect_dynasties,
    grade_trade,
)

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/teams", response_model=TeamRead)
def create_team(payload: TeamBase, db: Session = Depends(get_db)):
    team = Team(**payload.model_dump())
    db.add(team)
    db.commit()
    db.refresh(team)
    return team


@router.get("/teams", response_model=list[TeamRead])
def list_teams(db: Session = Depends(get_db)):
    return db.scalars(select(Team).order_by(Team.name)).all()


@router.post("/players", response_model=PlayerRead)
def create_player(payload: PlayerBase, db: Session = Depends(get_db)):
    player = Player(**payload.model_dump())
    db.add(player)
    db.commit()
    db.refresh(player)
    return player


@router.get("/players", response_model=list[PlayerRead])
def list_players(q: str | None = None, db: Session = Depends(get_db)):
    stmt = select(Player).order_by(Player.name)
    if q:
        stmt = stmt.where(Player.name.ilike(f"%{q}%"))
    return db.scalars(stmt).all()


@router.post("/player-seasons", response_model=PlayerSeasonRead)
def create_player_season(payload: PlayerSeasonBase, db: Session = Depends(get_db)):
    body = payload.model_dump()
    body["role_classification"] = payload.role_classification or classify_role(payload.overall_rating)
    season = PlayerSeason(**body)
    db.add(season)
    db.commit()
    db.refresh(season)
    return season


@router.get("/player-seasons/{player_id}", response_model=list[PlayerSeasonRead])
def get_player_seasons(player_id: int, db: Session = Depends(get_db)):
    return db.scalars(select(PlayerSeason).where(PlayerSeason.player_id == player_id).order_by(PlayerSeason.season_year)).all()


@router.post("/seasons", response_model=SeasonRead)
def create_season(payload: SeasonBase, db: Session = Depends(get_db)):
    season = Season(**payload.model_dump())
    db.add(season)
    db.commit()
    db.refresh(season)
    return season


@router.get("/seasons", response_model=list[SeasonRead])
def list_seasons(db: Session = Depends(get_db)):
    return db.scalars(select(Season).order_by(Season.year)).all()


@router.post("/trades", response_model=TradeRead)
def create_trade(payload: TradeBase, db: Session = Depends(get_db)):
    team_a_grade, _ = grade_trade(100, 20, 1, 0)
    trade = Trade(**payload.model_dump(), evaluation_grade=team_a_grade)
    db.add(trade)
    db.commit()
    db.refresh(trade)
    return trade


@router.get("/trades", response_model=list[TradeRead])
def list_trades(db: Session = Depends(get_db)):
    return db.scalars(select(Trade).order_by(Trade.trade_date.desc())).all()


@router.post("/draft-prospects", response_model=DraftProspectRead)
def create_draft_prospect(payload: DraftProspectBase, db: Session = Depends(get_db)):
    tier = analyze_draft_tier(payload.college_ppg, payload.college_rpg, payload.college_apg, payload.fg_pct)
    strengths = "Scoring versatility, positional IQ" if payload.college_ppg > 18 else "Motor and role fit"
    weaknesses = "Shot creation consistency" if payload.fg_pct < 0.45 else "Limited burst"
    prospect = DraftProspect(
        **payload.model_dump(),
        strengths=strengths,
        weaknesses=weaknesses,
        projected_ceiling="All-NBA",
        projected_floor="Rotation player",
        expected_tier=tier,
    )
    db.add(prospect)
    db.commit()
    db.refresh(prospect)
    return prospect


@router.get("/draft-prospects", response_model=list[DraftProspectRead])
def list_draft_prospects(draft_year: int | None = None, db: Session = Depends(get_db)):
    stmt = select(DraftProspect).order_by(DraftProspect.draft_year.desc())
    if draft_year:
        stmt = stmt.where(DraftProspect.draft_year == draft_year)
    return db.scalars(stmt).all()


@router.get("/analytics/legacy/{player_id}")
def get_legacy(player_id: int, db: Session = Depends(get_db)):
    return {"player_id": player_id, "legacy_score": compute_legacy_score(db, player_id)}


@router.get("/analytics/draft-outcome/{player_id}")
def get_draft_outcome(player_id: int, db: Session = Depends(get_db)):
    player = db.get(Player, player_id)
    if not player:
        raise HTTPException(status_code=404, detail="Player not found")
    seasons = db.scalars(select(PlayerSeason).where(PlayerSeason.player_id == player_id)).all()
    career_ppg = sum(s.ppg for s in seasons) / len(seasons) if seasons else 0
    outcome = classify_draft_outcome(player.draft_pick, career_ppg, all_star_count=0)
    return {"player_id": player_id, "career_ppg": round(career_ppg, 2), "outcome": outcome}


@router.get("/analytics/dynasties")
def get_dynasties(db: Session = Depends(get_db)):
    return detect_dynasties(db)


@router.get("/analytics/player-comparison/{player_a}/{player_b}", response_model=PlayerComparisonResponse)
def compare_players(player_a: int, player_b: int, db: Session = Depends(get_db)):
    a = db.get(Player, player_a)
    b = db.get(Player, player_b)
    if not a or not b:
        raise HTTPException(status_code=404, detail="One or both players not found")
    legacy_a = compute_legacy_score(db, player_a)
    legacy_b = compute_legacy_score(db, player_b)
    verdict = a.name if legacy_a >= legacy_b else b.name
    return PlayerComparisonResponse(player_a=a, player_b=b, legacy_a=legacy_a, legacy_b=legacy_b, verdict=verdict)
