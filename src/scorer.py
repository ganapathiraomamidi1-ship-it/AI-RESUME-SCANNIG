from __future__ import annotations

import re
from dataclasses import dataclass


DEFAULT_SKILLS = {
    "python", "java", "c", "c++", "sql", "mysql", "postgresql",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch",
    "machine learning", "deep learning", "data science", "data analysis",
    "power bi", "tableau", "excel", "statistics", "nlp", "git",
    "github", "docker", "aws", "azure", "spring boot", "react"
}


@dataclass
class ScanResult:
    score: float
    matched_skills: list[str]
    missing_skills: list[str]
    keyword_score: float
    experience_score: float


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9+#. ]+", " ", text.lower())


def score_resume(resume_text: str, job_description: str,
                 skills: set[str] | None = None) -> ScanResult:
    skills = skills or DEFAULT_SKILLS
    resume = normalize(resume_text)
    job = normalize(job_description)

    job_skills = sorted(
        skill for skill in skills
        if re.search(r"(?<!\w)" + re.escape(skill) + r"(?!\w)", job)
    )
    matched = [
        skill for skill in job_skills
        if re.search(r"(?<!\w)" + re.escape(skill) + r"(?!\w)", resume)
    ]
    missing = [skill for skill in job_skills if skill not in matched]

    keyword_score = 100.0 if not job_skills else 100 * len(matched) / len(job_skills)

    experience_terms = ["experience", "internship", "project", "years", "developer", "engineer"]
    experience_hits = sum(term in resume for term in experience_terms)
    experience_score = min(100.0, experience_hits / len(experience_terms) * 100)

    final_score = round(0.8 * keyword_score + 0.2 * experience_score, 2)

    return ScanResult(
        score=final_score,
        matched_skills=matched,
        missing_skills=missing,
        keyword_score=round(keyword_score, 2),
        experience_score=round(experience_score, 2),
    )
