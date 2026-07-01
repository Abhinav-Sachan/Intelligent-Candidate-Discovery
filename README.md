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

* Overview
* Problem Statement
* Features
* Scoring Methodology
* Project Architecture
* Project Structure
* Technologies Used
* Installation
* Running the Project
* Example Output
* Output
* Scalability
* Future Improvements
* Dataset
* Author
* License

---

# Problem Statement

Recruiters often receive thousands of applications for a single job opening.

Traditional Applicant Tracking Systems (ATS) primarily rely on keyword matching, which can:

* Miss qualified candidates
* Rank candidates inaccurately
* Ignore contextual experience
* Provide little or no explanation for rankings

This project addresses these challenges by combining semantic matching with a multi-factor scoring engine to produce transparent and explainable candidate rankings.

---

# Features

* Reads Job Descriptions from a DOCX file
* Supports datasets containing up to **100,000 candidate profiles**
* Parses candidate profiles from both JSON and JSONL formats
* Automatically extracts job requirements
* Performs semantic skill matching
* Scores candidates using five independent scoring modules
* Generates recruiter-friendly explanations
* Exports ranked candidates to CSV
* Modular and scalable Python architecture

---

# Scoring Methodology

Each candidate receives a score based on five independent evaluation modules.

| Module            | Purpose                             | Maximum Score |
| ----------------- | ----------------------------------- | ------------: |
| Experience        | Relevant years of experience        |            20 |
| Skills            | Technical and domain skill matching |            20 |
| Career            | Career progression and relevance    |            20 |
| Profile           | Semantic profile evaluation         |            20 |
| Recruiter Signals | Recruiter engagement and activity   |            20 |

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
                      CSV Export Output
```

---

# Project Structure

```text
Intelligent-Candidate-Discovery/
│
├── data/
│   ├── sample_candidates.json
│   ├── job_description.docx
│   └── candidates.jsonl (local only)
│
├── output/
│   └── ranked_candidates.csv
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

* Python 3
* JSON / JSONL
* python-docx
* CSV
* Rule-Based AI
* Semantic Matching
* Explainable AI
* Modular Software Design

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

* Load candidate profiles
* Load the job description
* Extract job requirements
* Score every candidate
* Rank all candidates
* Generate recruiter-friendly explanations
* Export the final rankings to:

```text
output/ranked_candidates.csv
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

Exporting CSV...
CSV exported successfully.

Project completed successfully!
```

---

# Output

The generated CSV contains:

* Candidate Rank
* Candidate ID
* Current Job Title
* Company
* Experience
* Individual Module Scores
* Total Score
* Explainable Ranking Summary

---

# Scalability

The system has been successfully tested on a dataset containing approximately **100,000 candidate profiles**.

Its modular architecture makes it easy to extend with:

* Machine Learning models
* Large Language Models (LLMs)
* Resume parsing
* Resume embeddings
* Vector search
* Cloud deployment
* REST APIs

---

# Future Improvements

Possible future enhancements include:

* LLM-assisted candidate evaluation
* Resume PDF parsing
* Embedding-based semantic search
* Interactive web dashboard
* Recruiter analytics
* REST API
* Docker deployment
* Real-time candidate recommendations

---

# Dataset

This project was developed and tested using a dataset containing approximately **100,000 candidate profiles**.

Due to GitHub's **100 MB file size limit**, the complete dataset is **not included** in this repository.

A smaller sample dataset (`sample_candidates.json`) is included for demonstration and testing purposes.

---

# Author

**Abhinav Sachan**

GitHub: https://github.com/Abhinav-Sachan

Developed as a hackathon project demonstrating AI-assisted candidate discovery, semantic matching, scalable candidate ranking, and explainable recruitment systems.

---

# License

This project is intended for educational purposes and hackathon submissions.
