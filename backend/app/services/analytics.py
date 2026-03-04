from __future__ import annotations

from collections import defaultdict
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.entities import AwardRecord, PlayerSeason, Season

LEGACY_WEIGHTS = {
    "CHAMPIONSHIP": 100,
    "FINALS_MVP": 70,
    "MVP": 80,
    "ALL_NBA": 25,
    "ALL_STAR": 10,
    "ALL_DEFENSE": 20,
    "ALL_ROOKIE": 10,
    "DPOY": 60,
    "MIP": 15,
}


def classify_role(overall: int) -> str:
    if overall < 75:
        return "Young Role Player"
    if overall < 80:
        return "Rotation Player"
    if overall < 85:
        return "Starter"
    if overall < 90:
        return "Star"
    return "Superstar"


def compute_legacy_score(db: Session, player_id: int) -> int:
    score = 0
    awards = db.scalars(select(AwardRecord).where(AwardRecord.player_id == player_id)).all()
    for award in awards:
        score += LEGACY_WEIGHTS.get(award.award_type.upper(), 0)

    seasons = db.scalars(select(PlayerSeason).where(PlayerSeason.player_id == player_id)).all()
    for season in seasons:
        if season.ppg >= 25:
            score += 8
        elif season.ppg >= 20:
            score += 5
        if season.rpg >= 10:
            score += 5
        if season.spg >= 2:
            score += 4
        if season.bpg >= 2:
            score += 4
        if season.ppg >= 25 and season.rpg >= 5 and season.apg >= 5:
            score += 10
    return score


def classify_draft_outcome(draft_pick: int, career_ppg: float, all_star_count: int) -> str:
    if draft_pick <= 14 and career_ppg < 6:
        return "Bust"
    if draft_pick <= 14 and career_ppg < 12:
        return "Underperformed"
    if draft_pick <= 14 and 15 <= career_ppg <= 20:
        return "Good Pick"
    if draft_pick > 30 and all_star_count > 0:
        return "Way Exceeded Expectations"
    if draft_pick > 14 and career_ppg >= 20:
        return "Exceeded Expectations"
    if career_ppg >= 20:
        return "Great Pick"
    if career_ppg >= 12:
        return "Decent Pick"
    return "Underperformed"


def detect_late_bloomer(ppg_progression: list[float]) -> bool:
    if len(ppg_progression) < 5:
        return False
    return ppg_progression[0] <= 3 and ppg_progression[-1] >= 18 and sorted(ppg_progression) == ppg_progression


def analyze_draft_tier(college_ppg: float, college_rpg: float, college_apg: float, fg_pct: float) -> str:
    composite = college_ppg * 0.45 + college_rpg * 0.2 + college_apg * 0.2 + fg_pct * 20 * 0.15
    if composite >= 24:
        return "Generational"
    if composite >= 20:
        return "Superstar"
    if composite >= 16:
        return "Star"
    if composite >= 13:
        return "Starter"
    return "Role Player"


def detect_dynasties(db: Session) -> list[dict]:
    seasons = db.scalars(select(Season).where(Season.champion_team_id.is_not(None)).order_by(Season.year)).all()
    champs_by_team: dict[int, list[int]] = defaultdict(list)
    for s in seasons:
        champs_by_team[s.champion_team_id].append(s.year)

    dynasties = []
    for team_id, years in champs_by_team.items():
        for i in range(len(years)):
            window = [y for y in years if years[i] <= y <= years[i] + 4]
            if len(window) >= 3:
                dynasties.append(
                    {
                        "team_id": team_id,
                        "start_year": window[0],
                        "end_year": window[-1],
                        "championships_won": len(window),
                    }
                )
                break
    return dynasties


def grade_trade(team_a_legacy_delta: int, team_b_legacy_delta: int, team_a_titles: int, team_b_titles: int) -> tuple[str, str]:
    def score(delta: int, titles: int) -> int:
        return delta + titles * 120

    a_score = score(team_a_legacy_delta, team_a_titles)
    b_score = score(team_b_legacy_delta, team_b_titles)

    def to_grade(v: int) -> str:
        if v >= 300:
            return "A"
        if v >= 180:
            return "B"
        if v >= 80:
            return "C"
        if v >= 0:
            return "D"
        return "F"

    return to_grade(a_score), to_grade(b_score)
