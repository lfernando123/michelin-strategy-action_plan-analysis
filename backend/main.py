from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from rag.loader import load_docx
from rag.embeddings import embed_documents
from rag.vector_store import build_index
from rag.retriever import retrieve_context
from rag.prompts import build_prompt

from rag.llm import call_ollama

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Strategy–Action RAG System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # allow React frontend
    allow_methods=["*"],
    allow_headers=["*"],
)


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

    if INDEX is None:
        return {"error": "Documents not indexed yet"}

    retrieved = retrieve_context(
        query=q.question,
        index=INDEX,
        documents=DOCUMENTS,
        model=MODEL,
        k=6
    )

    context = "\n".join(
        f"[{d['type'].upper()} | similarity={d['score']}]\n{d['text']}"
        for d in retrieved
    )

    prompt = build_prompt(q.question, context)

    # 🦙 OLLAMA LLM CALL (THIS IS THE G IN RAG)
    answer = call_ollama(prompt)

    return {
        "answer": answer,
        "evidence": retrieved
    }
