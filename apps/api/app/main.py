"""FastAPI entrypoint."""
import structlog
from fastapi import FastAPI
from app.core.config import settings

# Configure structured logging
structlog.configure(
    processors=[
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ]
)
logger = structlog.get_logger()

app = FastAPI(title=settings.app_name)

@app.get("/healthz")
def health_check():
    """Liveness probe."""
    logger.info("health_check_hit")
    return {"status": "ok", "environment": settings.environment}