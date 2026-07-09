import pandas as pd
from pypdf import PdfReader


def extract_pdf(file):
    """Extract text from PDF."""
    reader = PdfReader(file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def extract_txt(file):
    """Extract text from TXT."""
    return file.read().decode("utf-8")


def extract_csv(file):
    """Extract text from CSV."""
    df = pd.read_csv(file)
    return df.to_string(index=False)


def extract_text(uploaded_file):
    """Detect file type and extract text."""

    if uploaded_file is None:
        return ""

    extension = uploaded_file.name.split(".")[-1].lower()

    try:
        if extension == "pdf":
            return extract_pdf(uploaded_file)

        elif extension == "txt":
            return extract_txt(uploaded_file)

        elif extension == "csv":
            return extract_csv(uploaded_file)

        else:
            return "Unsupported file format."

    except Exception as e:
        return f"Error reading file: {e}"