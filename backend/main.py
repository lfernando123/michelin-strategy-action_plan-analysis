from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from rag.loader import load_docx
from rag.embeddings import embed_documents
from rag.vector_store import build_index
from rag.retriever import retrieve_context
from rag.prompts import build_prompt

app = FastAPI(title="Strategy–Action RAG System")

DOCUMENTS = []
INDEX = None
MODEL = None


@app.post("/upload")
async def upload_docs(
    strategy: UploadFile = File(...),
    action: UploadFile = File(...)
):
    global DOCUMENTS, INDEX, MODEL

    strategy_chunks = load_docx(strategy.file)
    action_chunks = load_docx(action.file)

    DOCUMENTS = (
        [{"type": "strategy", "text": t} for t in strategy_chunks] +
        [{"type": "action", "text": t} for t in action_chunks]
    )

    embeddings, MODEL = embed_documents(DOCUMENTS)
    INDEX = build_index(embeddings)

    return {"message": "Documents successfully indexed"}


class Question(BaseModel):
    question: str


@app.post("/ask")
def ask(q: Question):

    retrieved = retrieve_context(
        query=q.question,
        index=INDEX,
        documents=DOCUMENTS,
        model=MODEL,
        k=6
    )

    context = "\n".join(
        f"[{d['type'].upper()} | score={d['score']}]\n{d['text']}"
        for d in retrieved
    )

    prompt = build_prompt(q.question, context)

    # 🔁 Replace this with OpenAI / local LLM call
    answer = prompt

    return {
        "answer": answer,
        "evidence": retrieved
    }

