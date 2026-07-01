"""
scorer.py

Coordinates all scoring modules and ranks candidates.
"""

from scoring.experience import experience_score
from scoring.skills import skill_score
from scoring.career import career_score
from scoring.profile import profile_score
from scoring.signals import signal_score

from utils.explanation import generate_explanation
from utils.job_requirements import extract_job_requirements


def rank_candidates(candidates, job_description):
    """
    Rank candidates using extracted job requirements.
    """

    # -----------------------------
    # Extract JD requirements ONCE
    # -----------------------------
    requirements = extract_job_requirements(job_description)

    ranked_candidates = []

    for candidate in candidates:

        experience = experience_score(candidate, requirements)
        skills = skill_score(candidate, requirements)
        career = career_score(candidate, requirements)
        profile = profile_score(candidate, requirements)
        signals = signal_score(candidate, requirements)

        total_score = (
            experience
            + skills
            + career
            + profile
            + signals
        )

        explanation = generate_explanation(candidate)

        ranked_candidates.append({
            "candidate": candidate,
            "experience": experience,
            "skills": skills,
            "career": career,
            "profile": profile,
            "signals": signals,
            "total_score": total_score,
            "explanation": explanation
        })

    ranked_candidates.sort(
        key=lambda candidate: candidate["total_score"],
        reverse=True
    )

    return ranked_candidates