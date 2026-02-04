from sentence_transformers import SentenceTransformer
import numpy as np

MODEL_NAME = "all-MiniLM-L6-v2"

def embed_documents(documents):
    """
    Generates embeddings for documents
    """
    model = SentenceTransformer(MODEL_NAME)

    texts = [d["text"] for d in documents]
    embeddings = model.encode(texts, convert_to_numpy=True)

    return embeddings, model
