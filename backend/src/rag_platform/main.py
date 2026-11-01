
from fastapi import FastAPI
from rag_platform.api.v1.health import router as health_router

app = FastAPI(
    title="AI Document Intelligence API",
    description="Production-grade AI Document Intelligence and RAG Platform",
    version="0.1.0",
)

app.include_router(
    health_router,
    prefix="/api/v1",
)