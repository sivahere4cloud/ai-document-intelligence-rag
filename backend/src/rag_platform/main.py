from fastapi import FastAPI

app = FastAPI(
    title="AI Document Intelligence API",
    description="Production-grade AI Document Intelligence and RAG Platform",
    version="0.1.0",
)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}