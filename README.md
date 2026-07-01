# Intelligent Candidate Discovery

## AI-Powered Candidate Ranking System

An intelligent recruitment system that ranks job candidates using semantic analysis, structured profile evaluation, recruiter signals, and explainable AI scoring.

Instead of relying on simple keyword matching, the system analyzes candidate experience, skills, career history, profile quality, and recruiter engagement signals to identify the most suitable candidates for a given job description.

---

# Problem Statement

Recruiters often receive thousands of applications for a single job opening.

Traditional Applicant Tracking Systems (ATS) primarily rely on keyword matching, which can:

* Miss qualified candidates
* Rank candidates inaccurately
* Ignore contextual experience
* Provide little or no explanation for rankings

This project addresses these challenges by combining semantic matching with a multi-factor scoring engine to produce explainable candidate rankings.

---

# Features

* Reads Job Description from a DOCX file
* Supports datasets containing up to 100,000 candidates
* Parses candidate profiles from JSON and JSONL formats
* Extracts job requirements automatically
* Performs semantic skill matching
* Scores candidates using multiple independent modules
* Generates recruiter-friendly explanations
* Exports ranked candidates to CSV
* Modular and scalable architecture

---

# Scoring Methodology

Each candidate receives a score based on five independent components.

| Module            | Purpose                                    | Maximum Score |
| ----------------- | ------------------------------------------ | ------------: |
| Experience        | Relevant years of experience               |            20 |
| Skills            | Technical and domain skill matching        |            20 |
| Career            | Career progression and relevance           |            20 |
| Profile           | Profile completeness and semantic evidence |            20 |
| Recruiter Signals | Recruiter engagement and activity          |            20 |

**Maximum Total Score:** 100

---

# Project Architecture

```text
Job Description (.docx)
        │
        ▼
Job Requirement Extraction
        │
        ▼
Candidate Parser
        │
        ▼
Semantic Evidence Extraction
        │
        ▼
Scoring Engine
        │
        ▼
Candidate Ranking
        │
        ▼
Explanation Generator
        │
        ▼
CSV Export
```

---

# Project Structure

```text
Intelligent-Candidate-Discovery/
│
├── Data/
│   ├── candidates.jsonl
│   ├── sample_candidates.json
│   └── job_description.docx
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
└── README.md
```

---

# Technologies Used

* Python 3
* JSON / JSONL
* python-docx
* CSV
* Modular Software Design

---

# How to Run

### Install dependencies

```bash
pip install python-docx
```

### Run the project

```bash
python main.py
```

---

# Output

The system generates:

* Ranked candidate list
* Individual module scores
* Overall score
* Recruiter-friendly explanation
* CSV export in the `output/` folder

---

# Scalability

The system has been successfully tested on a dataset containing **100,000 candidate profiles**.

The modular architecture makes it easy to extend with:

* Machine Learning models
* Large Language Models (LLMs)
* Resume parsing
* Resume embeddings
* Vector search
* Cloud deployment
* API integration

---

# Future Improvements

* LLM-assisted candidate evaluation
* Resume PDF parsing
* Embedding-based semantic search
* Web dashboard
* Recruiter analytics
* REST API
* Real-time candidate recommendations

---

# Author

Developed as a hackathon project demonstrating AI-assisted candidate discovery, semantic matching, and explainable recruitment ranking.

## Dataset

This project was developed and tested using a dataset of approximately **100,000 candidate profiles**.

The full dataset is **not included in this repository** because it exceeds GitHub's file size limit (100 MB).

The repository includes a small sample dataset (`sample_candidates.json`) for testing and demonstration purposes.
