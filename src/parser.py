from pathlib import Path

from docx import Document
from pypdf import PdfReader


def extract_text(path: str) -> str:
    """Extract text from a PDF or DOCX resume."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(file_path)

    suffix = file_path.suffix.lower()
    if suffix == ".pdf":
        reader = PdfReader(str(file_path))
        return "\n".join(page.extract_text() or "" for page in reader.pages).strip()

    if suffix == ".docx":
        doc = Document(str(file_path))
        return "\n".join(p.text for p in doc.paragraphs).strip()

    raise ValueError("Supported resume formats: .pdf and .docx")
