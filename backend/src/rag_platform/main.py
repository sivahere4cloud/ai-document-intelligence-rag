
from fastapi import FastAPI
from rag_platform.api.v1.health import router as health_router
from rag_platform.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
)

app.include_router(
    health_router,
    prefix="/api/v1",
)