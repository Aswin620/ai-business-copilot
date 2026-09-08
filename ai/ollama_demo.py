import json
from urllib.request import Request, urlopen


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"

prompt = """
User: My company is ABC Technologies.
Assistant: Thanks. How can I help you?
User: What is my company name?
"""


data = {
    "model": MODEL,
    "prompt": prompt,
    "stream": False,
    "options": {
        "temperature": 0.8
    }
}

request = Request(
    OLLAMA_URL,
    data=json.dumps(data).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST"
)


with urlopen(request) as response:
    result = json.loads(response.read().decode("utf-8"))


print("Prompt:")
print(prompt)

print("\nLlama response:")
print(result["response"])