def build_prompt(question, context):
    return f"""
You are a senior strategy consultant.

Rules:
- Use ONLY the information in the CONTEXT
- Do NOT introduce assumptions
- Do NOT reference external frameworks

CONTEXT:
{context}

QUESTION:
{question}

Your response must include:
1. Alignment assessment
2. Gaps or overlaps
3. Improvement recommendations
4. Strategic risks if not addressed
"""
