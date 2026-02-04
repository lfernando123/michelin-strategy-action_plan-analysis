import faiss

def retrieve_context(query, index, documents, model, k=5):
    """
    Retrieves top-k relevant documents for a query
    """
    query_embedding = model.encode([query], convert_to_numpy=True)
    faiss.normalize_L2(query_embedding)

    scores, indices = index.search(query_embedding, k)

    results = []
    for idx, score in zip(indices[0], scores[0]):
        results.append({
            "text": documents[idx]["text"],
            "type": documents[idx]["type"],
            "score": round(float(score), 3)
        })

    return results

