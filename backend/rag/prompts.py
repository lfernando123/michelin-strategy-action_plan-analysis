def build_prompt(question, context):
    return f"""
You are an AI strategy consultant.

INSTRUCTIONS:
1. Use ONLY the information in CONTEXT.
2. Analyze alignment between Strategy and Action Plan.
3. If you find gaps, propose specific improvements:
   - New KPIs
   - Modified timelines
   - Missing tasks
4. Format your answer clearly:
   1. Alignment Summary
   2. Gaps / Misalignments
   3. Recommended Improvements (structured)
   4. Risks

CONTEXT:
{context}

USER QUESTION:
{question}
"""
