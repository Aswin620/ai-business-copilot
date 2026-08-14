import ollama

from app.config import settings


class OllamaService:
    def __init__(self):
        self.client = ollama.Client(
            host=settings.ollama_base_url
        )
        self.model = settings.ollama_model

    def generate(self, prompt: str) -> str:
        response = self.client.generate(
            model=self.model,
            prompt=prompt,
        )

        return response["response"]