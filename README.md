# AI Resume Scanner & ATS Analyzer 🤖

An explainable Python-based resume screening project that compares resumes with job descriptions, extracts relevant skills, identifies missing keywords, and produces an ATS-style match score.

## Features
- Resume skill extraction
- Job-description skill extraction
- Matched and missing skill analysis
- Explainable ATS-style scoring
- Email, phone, LinkedIn and GitHub signal checks
- Single-resume analysis
- Batch resume ranking
- JSON report generation

## Tech Stack
Python, pandas, NumPy, scikit-learn, PyPDF2, python-docx

## Installation
    pip install -r requirements.txt

## Analyze a Resume
    python src/resume_scanner.py --resume resume.txt --job job_description.txt

The analyzer generates an explainable JSON report under `outputs/`.

## Rank Multiple Resumes
Place TXT or Markdown resumes in a directory:

    python src/batch_scan.py --resumes resumes/ --job job_description.txt

## Scoring Method
The default ATS-style score uses 85% skill matching and 15% contact/profile completeness. The scoring is intentionally transparent and rule-based so the result can be explained.

**Important:** This is an educational portfolio project, not a validated hiring or employment decision system. It should not be used as the sole basis for recruiting decisions.

## Project Structure
    AI-RESUME-SCANNIG/
    ├── src/
    │   ├── resume_scanner.py
    │   └── batch_scan.py
    ├── job_description.txt
    ├── requirements.txt
    └── README.md

## Future Improvements
- PDF and DOCX resume parsing
- NLP embeddings for semantic matching
- Named-entity extraction
- Resume section classification
- Streamlit dashboard
- Explainable recommendations for missing skills
- Automated tests and benchmark dataset

## Author
Ganapathi Rao Mamidi