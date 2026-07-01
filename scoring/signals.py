"""
signals.py

Scores recruiter-related signals.
"""


def signal_score(candidate, requirements):
    """
    Calculate recruiter signal score.

    Args:
        candidate (dict)
        requirements (dict)

    Returns:
        int
    """

    signals = candidate.get("redrob_signals", {})

    score = 0

    if signals.get("open_to_work_flag"):
        score += 2

    if signals.get("recruiter_response_rate", 0) >= 0.80:
        score += 4

    if signals.get("github_activity_score", 0) >= 30:
        score += 3

    if signals.get("saved_by_recruiters_30d", 0) >= 10:
        score += 3

    if signals.get("search_appearance_30d", 0) >= 500:
        score += 3

    if signals.get("willing_to_relocate") and requirements.get("relocation"):
        score += 2

    if signals.get("preferred_work_mode", "").lower() == "flexible":
        score += 2

    if signals.get("verified_phone"):
        score += 1

    return min(score, 20)