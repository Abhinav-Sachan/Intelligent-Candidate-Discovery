"""
job_requirements.py

Extract important requirements from the Job Description.
"""

import re


def extract_job_requirements(job_description):
    """
    Extract important information from the job description.

    Args:
        job_description (str)

    Returns:
        dict
    """

    jd = job_description.lower()

    requirements = {
        "experience": None,
        "skills": [],
        "concepts": [],
        "leadership": False,
        "relocation": False,
        "hybrid": False
    }

    # -----------------------------------
    # Experience
    # -----------------------------------

    match = re.search(r"(\d+)\s*[-–]\s*(\d+)\s*years", jd)

    if match:
        requirements["experience"] = (
            int(match.group(1)),
            int(match.group(2))
        )

    # -----------------------------------
    # Skills
    # -----------------------------------

    known_skills = [
        "python",
        "machine learning",
        "deep learning",
        "nlp",
        "llm",
        "transformers",
        "retrieval",
        "embeddings",
        "recommendation",
        "ranking",
        "faiss",
        "pinecone",
        "mlflow",
        "hugging face",
        "scikit-learn",
        "feature engineering",
        "mlops"
    ]

    for skill in known_skills:

        if skill in jd:
            requirements["skills"].append(skill)

    # -----------------------------------
    # Concepts
    # -----------------------------------

    concepts = [
        "production",
        "evaluation",
        "deployment",
        "ownership",
        "experimentation",
        "search",
        "ranking"
    ]

    for concept in concepts:

        if concept in jd:
            requirements["concepts"].append(concept)

    # -----------------------------------
    # Leadership
    # -----------------------------------

    if any(word in jd for word in [
        "lead",
        "ownership",
        "mentor"
    ]):
        requirements["leadership"] = True

    # -----------------------------------
    # Relocation
    # -----------------------------------

    if "relocation" in jd:
        requirements["relocation"] = True

    # -----------------------------------
    # Hybrid
    # -----------------------------------

    if "hybrid" in jd:
        requirements["hybrid"] = True

    return requirements