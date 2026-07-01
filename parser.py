"""
parser.py

This module is responsible for reading all input files and converting
them into Python objects that the rest of the application can use.
"""

import json
from pathlib import Path

from docx import Document


# ==========================================================
# Data Folder
# ==========================================================

DATA_FOLDER = Path("Data")

CANDIDATE_JSONL = DATA_FOLDER / "candidates.jsonl"
CANDIDATE_JSON = DATA_FOLDER / "sample_candidates.json"
JOB_DESCRIPTION_FILE = DATA_FOLDER / "job_description.docx"


# ==========================================================
# Load Candidates
# ==========================================================

def load_candidates():
    """
    Load candidates from the real dataset if available.
    Otherwise load the sample dataset.
    """

    candidates = []

    # -----------------------------
    # Real Hackathon Dataset
    # -----------------------------
    if CANDIDATE_JSONL.exists():

        with open(CANDIDATE_JSONL, "r", encoding="utf-8") as file:

            for line in file:

                line = line.strip()

                if line:
                    candidates.append(json.loads(line))

        return candidates

    # -----------------------------
    # Sample Dataset
    # -----------------------------
    if CANDIDATE_JSON.exists():

        with open(CANDIDATE_JSON, "r", encoding="utf-8") as file:

            return json.load(file)

    raise FileNotFoundError(
        "No candidate dataset found."
    )


# ==========================================================
# Load Job Description
# ==========================================================

def load_job_description():
    """
    Read the job description DOCX file.

    Returns:
        str: Complete job description.
    """

    document = Document(JOB_DESCRIPTION_FILE)

    paragraphs = []

    for paragraph in document.paragraphs:

        text = paragraph.text.strip()

        if text:
            paragraphs.append(text)

    return "\n".join(paragraphs)