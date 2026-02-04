import faiss
import numpy as np

def build_index(embeddings):
    """
    Builds FAISS cosine similarity index
    """
    dimension = embeddings.shape[1]

    faiss.normalize_L2(embeddings)
    index = faiss.IndexFlatIP(dimension)
    index.add(embeddings)

    return index
