from docx import Document

def load_docx(file_obj):
    """
    Reads a DOCX file and returns cleaned text chunks
    """
    doc = Document(file_obj)
    chunks = []

    for para in doc.paragraphs:
        text = para.text.strip()
        if len(text) > 30:   # filter noise
            chunks.append(text)

    return chunks


