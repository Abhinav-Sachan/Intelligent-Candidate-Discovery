"""
parser.py

This module is responsible for reading all input files and converting
them into Python objects that the rest of the application can use.
"""

import gzip
import json
from pathlib import Path

from docx import Document


# ==========================================================
# Data Folder
# ==========================================================

DATA_FOLDER = Path("data")  # lowercase, matches README + repo structure

CANDIDATE_JSONL_GZ = DATA_FOLDER / "candidates.jsonl.gz"
CANDIDATE_JSONL = DATA_FOLDER / "candidates.jsonl"
CANDIDATE_JSON = DATA_FOLDER / "sample_candidates.json"
JOB_DESCRIPTION_FILE = DATA_FOLDER / "job_description.docx"


# ==========================================================
# Load Candidates
# ==========================================================

def load_candidates():
    """
    Load candidates in this priority order:
    1. Compressed real hackathon dataset (candidates.jsonl.gz)
    2. Uncompressed real dataset (candidates.jsonl)
    3. Sample dataset (sample_candidates.json)
    """

    candidates = []

    # -----------------------------
    # Real Hackathon Dataset (compressed)
    # -----------------------------
    if CANDIDATE_JSONL_GZ.exists():

        with gzip.open(CANDIDATE_JSONL_GZ, "rt", encoding="utf-8") as file:

            for line in file:

                line = line.strip()

                if line:
                    candidates.append(json.loads(line))

        return candidates

    # -----------------------------
    # Real Hackathon Dataset (uncompressed)
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
        "No candidate dataset found. Expected one of: "
        f"{CANDIDATE_JSONL_GZ}, {CANDIDATE_JSONL}, {CANDIDATE_JSON}"
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