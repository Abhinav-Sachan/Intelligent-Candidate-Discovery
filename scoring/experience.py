"""
experience.py

Scores a candidate based on the experience
required by the Job Description.
"""


def experience_score(candidate, requirements):
    """
    Calculate the experience score.

    Args:
        candidate (dict): Candidate information.
        requirements (dict): Extracted job requirements.

    Returns:
        int: Experience score (0-20)
    """

    years = (
        candidate
        .get("profile", {})
        .get("years_of_experience", 0)
    )

    experience_range = requirements.get("experience")

    # If no experience range was found in the JD,
    # give a neutral score.
    if experience_range is None:
        return 10

    minimum_years, maximum_years = experience_range

    # Perfect match
    if minimum_years <= years <= maximum_years:
        return 20

    # Slightly below requirement
    elif years >= minimum_years - 1:
        return 15

    # Slightly above requirement
    elif years <= maximum_years + 2:
        return 15

    # Too little experience
    elif years < minimum_years:
        return 8

    # Overqualified
    else:
        return 10