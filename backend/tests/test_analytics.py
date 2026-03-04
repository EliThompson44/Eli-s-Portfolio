from app.services.analytics import (
    classify_draft_outcome,
    detect_late_bloomer,
    is_dynasty,
    legacy_points,
)


def test_legacy_points() -> None:
    score = legacy_points({"championships": 2, "mvps": 1, "all_star": 10})
    assert score == 380


def test_draft_outcome_late_pick_star() -> None:
    outcome = classify_draft_outcome(draft_pick=45, career_ppg=22.1, all_star_appearances=3)
    assert outcome == "Way Exceeded Expectations"


def test_late_bloomer_detection() -> None:
    assert detect_late_bloomer([2, 4, 6, 14, 20]) is True


def test_dynasty_detection() -> None:
    assert is_dynasty([1961, 1963, 1965], 1965) is True
