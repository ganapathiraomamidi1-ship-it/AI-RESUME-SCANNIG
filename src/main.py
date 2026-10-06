from __future__ import annotations

import argparse
from pathlib import Path

from parser import extract_text
from scorer import score_resume


def main() -> None:
    parser = argparse.ArgumentParser(description="AI/ATS-style resume scanner")
    parser.add_argument("--resume", required=True, help="PDF or DOCX resume")
    parser.add_argument("--job", required=True, help="Text file containing the job description")
    args = parser.parse_args()

    resume_text = extract_text(args.resume)
    job_description = Path(args.job).read_text(encoding="utf-8")
    result = score_resume(resume_text, job_description)

    print("\nAI RESUME SCANNER")
    print("=" * 40)
    print(f"Overall ATS-style score : {result.score:.2f}/100")
    print(f"Keyword match score     : {result.keyword_score:.2f}/100")
    print(f"Experience signal score : {result.experience_score:.2f}/100")
    print("\nMatched skills:")
    print(", ".join(result.matched_skills) or "None detected")
    print("\nMissing job skills:")
    print(", ".join(result.missing_skills) or "None detected")
    print("\nNote: This is an explainable screening aid, not a hiring decision system.")


if __name__ == "__main__":
    main()
