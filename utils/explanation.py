"""
explanation.py

Generate recruiter-friendly explanations for why a
candidate was ranked highly.
"""

from utils.evidence import extract_candidate_evidence


def generate_explanation(candidate):

    evidence = extract_candidate_evidence(candidate)

    explanation = []

    # Experience
    if evidence["experience_years"] >= 5:
        explanation.append(
            f'{evidence["experience_years"]} years of experience matches the job requirement.'
        )

    # Production ML
    if evidence["production_ml"]:
        explanation.append(
            "Has experience building production AI/ML systems."
        )

    # Retrieval
    if evidence["retrieval"]:
        explanation.append(
            "Has worked on search, retrieval, or embedding systems."
        )

    # Recommendation
    if evidence["recommendation"]:
        explanation.append(
            "Has recommendation and ranking system experience."
        )

    # NLP
    if evidence["nlp"]:
        explanation.append(
            "Has Natural Language Processing expertise."
        )

    # Evaluation
    if evidence["evaluation"]:
        explanation.append(
            "Has experience evaluating machine learning models."
        )

    # MLOps
    if evidence["mlops"]:
        explanation.append(
            "Has MLOps and deployment-related skills."
        )

    # Leadership
    if evidence["leadership"]:
        explanation.append(
            "Has demonstrated ownership or leadership."
        )

    # Recruiter Signals
    if evidence["strong_recruiter_signals"]:
        explanation.append(
            "Has strong recruiter engagement signals."
        )

    return explanation