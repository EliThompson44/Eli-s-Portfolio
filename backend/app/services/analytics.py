from statistics import mean


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


def generate_archetype(speed: int, shooting: int, defense: int, passing: int, rebounding: int, athleticism: int) -> str:
    if defense >= 85 and shooting >= 78 and speed >= 75:
        return "3 and D Wing"
    if passing >= 85 and speed >= 82:
        return "Playmaking Guard"
    if shooting >= 85 and rebounding >= 75 and athleticism >= 70:
        return "Stretch Big"
    if defense >= 90 and rebounding >= 85:
        return "Defensive Anchor"
    if passing >= 80 and size_score(rebounding, defense) >= 80:
        return "Point Forward"
    if rebounding >= 88 and shooting <= 70:
        return "Inside Scoring Center"
    return "Two Way Slashing Wing"


def size_score(rebounding: int, defense: int) -> float:
    return (rebounding + defense) / 2


def classify_draft_outcome(draft_pick: int, career_ppg: float, all_star_appearances: int = 0) -> str:
    if draft_pick > 30 and all_star_appearances > 0:
        return "Way Exceeded Expectations"
    if draft_pick > 20 and career_ppg >= 20:
        return "Exceeded Expectations"
    if draft_pick <= 14 and career_ppg < 6:
        return "Bust"
    if draft_pick <= 14 and 15 <= career_ppg <= 20:
        return "Good Pick"
    if career_ppg >= 20:
        return "Great Pick"
    if career_ppg >= 12:
        return "Decent Pick"
    return "Underperformed"


def detect_late_bloomer(scoring_by_year: list[float]) -> bool:
    if len(scoring_by_year) < 5:
        return False
    first_half = mean(scoring_by_year[:3])
    second_half = mean(scoring_by_year[-2:])
    return first_half <= 6 and second_half >= 16


def detect_bust_trend(scoring_by_year: list[float]) -> bool:
    if len(scoring_by_year) < 4:
        return False
    return all(scoring_by_year[i] >= scoring_by_year[i + 1] for i in range(len(scoring_by_year) - 1))


def legacy_points(payload: dict[str, int]) -> int:
    weights = {
        "championships": 100,
        "finals_mvps": 70,
        "mvps": 80,
        "all_nba": 25,
        "all_star": 10,
        "all_defense": 20,
        "all_rookie": 10,
        "dpoy": 60,
        "mip": 15,
        "seasons_25_ppg": 8,
        "seasons_20_ppg": 5,
        "seasons_double_double": 6,
        "seasons_10_reb": 5,
        "seasons_2_stl": 4,
        "seasons_2_blk": 4,
        "seasons_25_5_5": 10,
    }
    return sum(payload.get(key, 0) * value for key, value in weights.items())


def is_dynasty(championship_years: list[int], target_year: int) -> bool:
    window = [year for year in championship_years if target_year - 4 <= year <= target_year]
    return len(window) >= 3


def hall_of_fame_qualified(seasons_with_team: int, top_five_scorer: bool, finals_mvp_for_team: bool) -> bool:
    return seasons_with_team >= 8 or top_five_scorer or finals_mvp_for_team


def trade_grade(legacy_delta: float, championships_won: int, star_development_count: int) -> str:
    score = legacy_delta + (championships_won * 25) + (star_development_count * 10)
    if score >= 80:
        return "A"
    if score >= 50:
        return "B"
    if score >= 20:
        return "C"
    if score >= 0:
        return "D"
    return "F"
