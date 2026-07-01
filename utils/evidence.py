"""
evidence.py

Extract structured evidence from a candidate profile
using semantic concepts.
"""

from utils.semantic_dictionary import SEMANTIC_CONCEPTS


def extract_candidate_evidence(candidate):

    profile = candidate.get("profile", {})
    skills = candidate.get("skills", [])
    signals = candidate.get("redrob_signals", {})

    summary = profile.get("summary", "").lower()
    current_title = profile.get("current_title", "").lower()

    skill_names = [
        skill.get("name", "").lower()
        for skill in skills
    ]

    searchable_text = (
        summary +
        " " +
        current_title +
        " " +
        " ".join(skill_names)
    )

    evidence = {}

    # -----------------------------
    # Semantic Concept Matching
    # -----------------------------

    for concept, words in SEMANTIC_CONCEPTS.items():

        evidence[concept] = any(
            word.lower() in searchable_text
            for word in words
        )

    # -----------------------------
    # Recruiter Signals
    # -----------------------------

    evidence["strong_recruiter_signals"] = (
        signals.get("recruiter_response_rate", 0) >= 0.80
        and
        signals.get("saved_by_recruiters_30d", 0) >= 10
    )

    evidence["experience_years"] = profile.get(
        "years_of_experience",
        0
    )

    return evidence