from fastapi import FastAPI
from app.services.ollama_service import OllamaService

from app.api.routes.health import router as health_router
from app.config import settings
from app.api.routes.database import router as database_router
from app.api.routes.chat import router as chat_router
from app.api.routes import health
from app.api.routes import conversations
from fastapi import Request


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

app.include_router(
    database_router,
    prefix="/api/v1",
    tags=["Database"],
)

app.include_router(
    chat_router,
    prefix="/api/v1",
    tags=["Chat"],
)



app.include_router(health.router)   
app.include_router(conversations.router)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(
        f"{request.method} {request.url.path}"
    )

    response = await call_next(request)

    print(
        f"{request.method} {request.url.path} "
        f"-> {response.status_code}"
    )

    return response