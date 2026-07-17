from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat import router as chat_router
from app.auth.auth import router as auth_router
from app.api.conversation import router as conversation_router
from app.api.analytics import router as analytics_router
from app.api.upload import router as upload_router

app = FastAPI(
    title="Enterprise AI Chatbot",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://YOUR-VERCEL-APP.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "status": "running",
        "project": "Enterprise AI Chatbot"
    }

app.include_router(chat_router)
app.include_router(auth_router)
app.include_router(conversation_router)
app.include_router(analytics_router)
app.include_router(upload_router)