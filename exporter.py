"""
exporter.py

Exports ranked candidates to a CSV file.
"""

import csv
import os


OUTPUT_FILE = "output/ranked_candidates.csv"


def export_rankings(ranked_candidates):
    """
    Export ranked candidates to CSV.

    Args:
        ranked_candidates (list): Ranked candidate data.
    """

    os.makedirs("output", exist_ok=True)

    with open(
        OUTPUT_FILE,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Rank",
            "Candidate ID",
            "Current Title",
            "Current Company",
            "Experience (Years)",
            "Experience Score",
            "Skills Score",
            "Career Score",
            "Profile Score",
            "Signal Score",
            "Total Score",
            "Explanation"
        ])

        for rank, result in enumerate(ranked_candidates, start=1):

            candidate = result["candidate"]

            profile = candidate.get("profile", {})

            explanation = " | ".join(result["explanation"])

            writer.writerow([
                rank,
                candidate.get("candidate_id"),
                profile.get("current_title"),
                profile.get("current_company"),
                profile.get("years_of_experience"),
                result["experience"],
                result["skills"],
                result["career"],
                result["profile"],
                result["signals"],
                result["total_score"],
                explanation
            ])