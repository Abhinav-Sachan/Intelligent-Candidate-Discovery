# Intelligent Candidate Discovery

### AI-Powered Candidate Ranking System using Semantic Matching and Explainable Scoring

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Dataset](https://img.shields.io/badge/Dataset-100K%20Candidates-red)
![AI](https://img.shields.io/badge/AI-Explainable%20Ranking-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# Overview

Intelligent Candidate Discovery is an AI-powered recruitment system that ranks job candidates using semantic analysis, structured profile evaluation, recruiter engagement signals, and explainable AI scoring.

Instead of relying solely on keyword matching, the system evaluates candidate experience, technical skills, career history, profile quality, and recruiter signals to identify the most suitable candidates for a given job description.

The project is designed to efficiently process **large-scale recruitment datasets containing up to 100,000 candidate profiles** while providing transparent explanations for every ranking decision.

---

# Table of Contents

- Overview
- Problem Statement
- Features
- Scoring Methodology
- Project Architecture
- Project Structure
- Technologies Used
- Installation
- Running the Project
- Example Output
- Output
- Scalability
- Future Improvements
- Dataset
- Author
- License

---

# Problem Statement

Recruiters often receive thousands of applications for a single job opening.

Traditional Applicant Tracking Systems (ATS) primarily rely on keyword matching, which can:

- Miss qualified candidates
- Rank candidates inaccurately
- Ignore contextual experience
- Provide little or no explanation for rankings

This project addresses these challenges by combining semantic matching with a multi-factor scoring engine to produce transparent, explainable, and scalable candidate rankings.

---

# Features

- Reads Job Descriptions from a DOCX file
- Supports datasets containing up to **100,000 candidate profiles**
- Parses candidate profiles from both JSON and JSONL formats
- Automatically extracts job requirements
- Performs semantic skill matching
- Scores candidates using five independent scoring modules
- Generates recruiter-friendly explanations
- Exports ranked candidates to **Excel (.xlsx)** format
- Modular and scalable Python architecture

---

# Scoring Methodology

Each candidate receives a score based on five independent evaluation modules.

| Module | Purpose | Maximum Score |
|---------|---------|--------------:|
| Experience | Relevant years of experience | 20 |
| Skills | Technical and domain skill matching | 20 |
| Career | Career progression and relevance | 20 |
| Profile | Semantic profile evaluation | 20 |
| Recruiter Signals | Recruiter engagement and activity | 20 |

**Maximum Total Score: 100**

---

# Project Architecture

```text
                    Job Description (.docx)
                              │
                              ▼
              Job Requirement Extraction
                              │
                              ▼
                  Candidate Data Parser
                              │
                              ▼
              Semantic Evidence Extraction
                              │
                              ▼
                     Scoring Engine
        ┌──────────┬──────────┬──────────┬──────────┬──────────┐
        │Experience│  Skills  │ Career   │ Profile  │ Signals  │
        └──────────┴──────────┴──────────┴──────────┴──────────┘
                              │
                              ▼
                  Candidate Ranking Engine
                              │
                              ▼
                Explanation Generator
                              │
                              ▼
               Excel (.xlsx) Export Output
```

---

# Project Structure

```text
Intelligent-Candidate-Discovery/
│
├── data/
│   ├── sample_candidates.json
│   └── job_description.docx
│
├── output/
│   └── ranked_candidates.xlsx
│
├── scoring/
│   ├── career.py
│   ├── experience.py
│   ├── profile.py
│   ├── signals.py
│   └── skills.py
│
├── utils/
│   ├── evidence.py
│   ├── explanation.py
│   ├── job_requirements.py
│   └── semantic_dictionary.py
│
├── exporter.py
├── main.py
├── parser.py
├── scorer.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Technologies Used

- Python 3
- JSON / JSONL
- python-docx
- openpyxl (Excel Export)
- Rule-Based AI
- Semantic Matching
- Explainable AI
- Modular Software Design

---

# Installation

Clone the repository:

```bash
git clone https://github.com/Abhinav-Sachan/Intelligent-Candidate-Discovery.git
```

Move into the project directory:

```bash
cd Intelligent-Candidate-Discovery
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Execute the following command:

```bash
python main.py
```

The application will:

- Load candidate profiles
- Load the job description
- Extract job requirements
- Score every candidate
- Rank all candidates
- Generate recruiter-friendly explanations
- Export the final rankings to:

```text
output/ranked_candidates.xlsx
```

---

# Example Output

```text
Loading candidates...
100000 candidates loaded.

Loading Job Description...
Job Description loaded.

Ranking candidates...
Ranking completed.

Exporting Excel...
Excel exported successfully.

Project completed successfully!
```

---

# Output

The generated Excel (.xlsx) file contains:

- Candidate Rank
- Candidate ID
- Current Job Title
- Current Company
- Years of Experience
- Individual Module Scores
- Overall Score
- Explainable Ranking Summary

The exported workbook includes:

- Bold header row
- Auto-adjusted column widths
- Filter support
- Frozen header row for easier navigation

---

# Scalability

The system has been successfully tested on a dataset containing approximately **100,000 candidate profiles**.

The architecture is designed to scale efficiently for large recruitment datasets by using:

- Modular scoring components
- Efficient JSONL parsing
- Rule-based semantic matching
- Explainable scoring pipeline
- Lightweight processing without requiring machine learning models

---

# Future Improvements

Possible future enhancements include:

- LLM-assisted candidate evaluation
- Resume PDF parsing
- Embedding-based semantic search
- Interactive web dashboard
- Recruiter analytics
- REST API
- Docker deployment
- Cloud deployment
- Real-time candidate recommendations
- Vector database integration (FAISS/Pinecone)
- Hybrid semantic + embedding ranking

---

# Dataset

This project supports datasets containing up to **100,000 candidate profiles**.

Due to GitHub's **100 MB file size limit**, the complete dataset is **not included** in this repository.

A smaller sample dataset (`sample_candidates.json`) is included for demonstration and testing purposes.

When a `candidates.jsonl` file is placed inside the `data/` directory, the application automatically detects it and processes the full dataset without requiring any code changes.

---

# Why This Project?

This project demonstrates how explainable AI techniques can improve traditional Applicant Tracking Systems (ATS) by moving beyond simple keyword matching.

The ranking engine evaluates multiple aspects of a candidate profile—including experience, skills, career progression, semantic relevance, and recruiter engagement—to provide recruiters with transparent, data-driven recommendations.

The modular architecture also makes it straightforward to integrate machine learning models, vector search, or large language models in future versions.

---

# Author

**Abhinav Sachan**

GitHub: https://github.com/Abhinav-Sachan

Developed as a hackathon project demonstrating:

- AI-assisted candidate discovery
- Semantic candidate matching
- Explainable AI ranking
- Scalable recruitment systems
- Modular Python software engineering

---

# License

This project is licensed under the MIT License.

You are free to use, modify, and distribute this project in accordance with the terms of the MIT License.

---

## Repository Notes

The repository contains:

- Complete source code
- Sample dataset for testing
- Professional documentation
- Excel (.xlsx) export support
- Modular and extensible project structure

The large production dataset (100,000 candidate profiles) is intentionally excluded because it exceeds GitHub's maximum file size limit.