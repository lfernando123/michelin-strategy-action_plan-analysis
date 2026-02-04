import ollama

def call_ollama(prompt, model="qwen:1.8b"):
    """
    Calls Ollama LLM with a grounded RAG prompt
    """
    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
