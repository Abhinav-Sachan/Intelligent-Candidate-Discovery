"""
main.py

Entry point of the Intelligent Candidate Discovery project.
"""

from parser import load_candidates, load_job_description
from scorer import rank_candidates
from exporter import export_rankings


def main():

    # -----------------------------
    # Load Candidates
    # -----------------------------
    print("Loading candidates...")

    candidates = load_candidates()

    print(f"{len(candidates)} candidates loaded.")
    print()

    # -----------------------------
    # Load Job Description
    # -----------------------------
    print("Loading Job Description...")

    job_description = load_job_description()

    print("Job Description loaded.")
    print()

    # -----------------------------
    # Rank Candidates
    # -----------------------------
    print("Ranking candidates...")

    ranked_candidates = rank_candidates(
        candidates,
        job_description
    )

    print("Ranking completed.")
    print()

    # -----------------------------
    # Export Results
    # -----------------------------
    print("Exporting Excel...")

    export_rankings(ranked_candidates)

    print("Excel exported successfully.")
    print()

    print("Project completed successfully!")


if __name__ == "__main__":
    main()