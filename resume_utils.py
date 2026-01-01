from PyPDF2 import PdfReader
from docx import Document


def extract_text_from_pdf(file) -> str:
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def extract_text_from_docx(file) -> str:
    doc = Document(file)
    return "\n".join([para.text for para in doc.paragraphs])


def extract_resume_text(upload_file) -> str:
    filename = upload_file.filename.lower()

    if filename.endswith(".pdf"):
        return extract_text_from_pdf(upload_file.file)

    if filename.endswith(".docx"):
        return extract_text_from_docx(upload_file.file)

    raise ValueError("Unsupported file type. Upload PDF or DOCX only.")
