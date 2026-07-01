"""
profile.py

Scores a candidate's profile using semantic evidence.
"""

from utils.evidence import extract_candidate_evidence


def profile_score(candidate, requirements):

    evidence = extract_candidate_evidence(candidate)

    required_concepts = requirements.get("concepts", [])

    score = 0

    # Production ML
    if evidence["production_ml"] and "production" in required_concepts:
        score += 4

    # Retrieval / Search
    if evidence["retrieval"] and "search" in required_concepts:
        score += 4

    # Recommendation / Ranking
    if evidence["recommendation"] and "ranking" in required_concepts:
        score += 4

    # Evaluation
    if evidence["evaluation"] and "evaluation" in required_concepts:
        score += 3

    # Leadership
    if evidence["leadership"] and requirements.get("leadership"):
        score += 3

    # MLOps
    if evidence["mlops"]:
        score += 2

    return min(score, 20)