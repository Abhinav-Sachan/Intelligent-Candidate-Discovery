"""
main.py

Entry point of the Intelligent Candidate Discovery project.
"""

from parser import load_candidates, load_job_description
from scorer import rank_candidates
from exporter import export_rankings


# Number of top-ranked candidates to include in the final shortlist
TOP_N = 500


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

    # Keep only the top recommended candidates for the final shortlist
    ranked_candidates = ranked_candidates[:TOP_N]

    print(f"Ranking completed. Exporting top {TOP_N} candidates.")
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