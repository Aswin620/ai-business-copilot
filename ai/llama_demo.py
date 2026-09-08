import requests


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"


def generate_response(prompt: str):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False,
        },
        timeout=120,
    )

    response.raise_for_status()

    data = response.json()

    return data["response"]


if __name__ == "__main__":
    prompt = "Explain self-attention in simple terms."

    print("Prompt:")
    print(prompt)

    print("\nLlama response:")
    print(generate_response(prompt))