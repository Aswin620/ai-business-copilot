from fastapi import FastAPI
from app.services.ollama_service import OllamaService

from app.api.routes.health import router as health_router
from app.config import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI-powered business operations assistant.",
)


@app.get("/api/v1/ai/test")
def test_ai():
    ollama_service = OllamaService()

    response = ollama_service.generate(
        "Reply with exactly: Local Llama connection successful."
    )

    return {
        "model": settings.ollama_model,
        "response": response,
    }

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"],
)