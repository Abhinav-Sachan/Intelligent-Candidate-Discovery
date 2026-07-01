"""
career.py

Scores a candidate's career history using semantic evidence.
"""

from utils.evidence import extract_candidate_evidence


def career_score(candidate, requirements):
    """
    Calculate career score.

    Args:
        candidate (dict)
        requirements (dict)

    Returns:
        int
    """

    evidence = extract_candidate_evidence(candidate)

    score = 0

    career_history = candidate.get("career_history", [])

    # Stable career progression
    if len(career_history) >= 3:
        score += 5

    # Leadership
    if requirements.get("leadership") and evidence["leadership"]:
        score += 5

    # Production ML Experience
    if evidence["production_ml"]:
        score += 5

    # MLOps Experience
    if evidence["mlops"]:
        score += 5

    return min(score, 20)