import ollama

from app.config import settings


class OllamaService:
    def __init__(self) -> None:
        self.client = ollama.Client(
            host=settings.ollama_base_url
        )

        self.model = settings.ollama_model

    def chat(self, messages: list[dict[str, str]]) -> str:
        response = self.client.chat(
            model=self.model,
            messages=messages,
        )

        return response["message"]["content"]