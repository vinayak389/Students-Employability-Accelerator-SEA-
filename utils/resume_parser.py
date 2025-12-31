from pypdf import PdfReader
from docx import Document
from pathlib import Path

def extract_resume_text(file_path: str) -> str:
    path = Path(file_path)

    if path.suffix.lower() == ".pdf":
        return _extract_pdf(path)

    elif path.suffix.lower() == ".docx":
        return _extract_docx(path)

    else:
        raise ValueError("Unsupported file format. Upload PDF or DOCX only.")


def _extract_pdf(path: Path) -> str:
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text.strip()


def _extract_docx(path: Path) -> str:
    doc = Document(path)
    return "\n".join(p.text for p in doc.paragraphs).strip()
