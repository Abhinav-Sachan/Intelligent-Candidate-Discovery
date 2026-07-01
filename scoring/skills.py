"""
skills.py

Scores a candidate based on the skills required
by the Job Description.
"""


def skill_score(candidate, requirements):
    """
    Calculate the skills score.

    Args:
        candidate (dict): Candidate information.
        requirements (dict): Extracted job requirements.

    Returns:
        int: Skills score (0-20)
    """

    score = 0

    candidate_skills = candidate.get("skills", [])

    required_skills = requirements.get("skills", [])

    proficiency_points = {
        "beginner": 1,
        "intermediate": 2,
        "advanced": 3,
        "expert": 4
    }

    matched_skills = 0

    for skill in candidate_skills:

        skill_name = skill.get("name", "").lower()

        if skill_name in required_skills:

            matched_skills += 1

            score += proficiency_points.get(
                skill.get("proficiency", "").lower(),
                0
            )

            if skill.get("duration_months", 0) >= 24:
                score += 1

            if skill.get("endorsements", 0) >= 20:
                score += 1

    # Bonus for matching many required skills
    if matched_skills >= 5:
        score += 2
    elif matched_skills >= 3:
        score += 1

    return min(score, 20)