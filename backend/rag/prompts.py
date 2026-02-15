def build_prompt(question, context):
    return f"""
You are a strategic alignment analyst.

Analyze the alignment between the Strategy and Action Plan.

Return your answer STRICTLY in this JSON format:

{{
  "alignment_score": <number between 0 and 100>,
  "summary": "<short explanation>",
  "gaps": "<main misalignments>",
  "recommendations": "<specific improvements including KPIs, timelines, missing tasks>"
}}

CONTEXT:
{context}

QUESTION:
{question}
"""

