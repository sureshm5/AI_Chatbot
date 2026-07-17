from fastapi import APIRouter, UploadFile, File
import os

from app.rag.pdf_loader import load_pdf
from app.rag.chunker import chunk_text
from app.rag.embedder import embed
from app.rag.vector_store import add_vectors

router = APIRouter(
    prefix="/upload",
    tags=["RAG"]
)


UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):

    filepath = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(filepath, "wb") as f:

        f.write(await file.read())

    text = load_pdf(filepath)

    chunks = chunk_text(text)

    vectors = embed(chunks)

    add_vectors(vectors, chunks)

    return {

        "filename": file.filename,

        "chunks": len(chunks),

        "status": "Indexed Successfully"

    }