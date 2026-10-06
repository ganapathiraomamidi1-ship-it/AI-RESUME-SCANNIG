# AI Resume Scanner & ATS Analyzer 🤖📄

An explainable Python resume-screening project that extracts text from PDF/DOCX resumes and compares it with a job description to produce an ATS-style compatibility score.

> **Important:** Educational screening aid only. It should not be used as the sole basis for employment decisions or to infer protected/sensitive characteristics.

## Features

- PDF resume extraction with **pypdf**
- DOCX resume extraction with **python-docx**
- Job-description skill detection
- Resume-to-job skill matching
- ATS-style compatibility score
- Matched and missing skill report
- Experience-related keyword signal
- Explainable scoring
- Command-line interface

## Tech Stack

**Python · NLP-style text processing · Regular Expressions · pandas · scikit-learn · pypdf · python-docx**

## Project Structure

    AI-RESUME-SCANNIG/
    ├── src/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── parser.py
    │   └── scorer.py
    ├── job_description.txt
    ├── requirements.txt
    ├── .gitignore
    ├── LICENSE
    └── README.md

## Installation

    git clone https://github.com/ganapathiraomamidi1-ship-it/AI-RESUME-SCANNIG.git
    cd AI-RESUME-SCANNIG
    python -m venv .venv

Windows:

    .venv\Scripts\activate

macOS/Linux:

    source .venv/bin/activate

Install packages:

    pip install -r requirements.txt

## Run

Place a PDF or DOCX resume in the project directory:

    python src/main.py --resume your_resume.pdf --job job_description.txt

The scanner reports:

- Overall ATS-style score
- Keyword match score
- Experience signal score
- Matched skills
- Missing job skills

## Scoring Method

The current transparent baseline uses:

- **80% skill/keyword match**
- **20% experience-related language signal**

The skill score is calculated from skills detected in the job description and whether those skills appear in the resume.

This is intentionally simple and explainable. The score is **not** a probability of getting hired and does not measure a person's actual ability.

## Future Improvements

- TF-IDF + cosine similarity
- Sentence-transformer semantic similarity
- Skill taxonomy and synonym matching
- Resume section detection
- Missing-keyword recommendations
- Streamlit web interface
- JSON/PDF reports
- Unit tests and benchmark dataset
- Bias/fairness evaluation

## Portfolio Skills Demonstrated

Python, NLP, text preprocessing, feature engineering, explainable AI, document processing, machine-learning concepts, Git and GitHub.

## Author

**Ganapathi Rao Mamidi**
