import json
from urllib.request import Request, urlopen


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"


def ask_llama(prompt):
    data = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2
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

    return result["response"]


# --------------------------------------------------
# Experiment 1: Strict Output
# --------------------------------------------------

def strict_output_demo():
    prompt = """
You are an AI Business Operations Assistant.

Explain what a CRM is.

STRICT OUTPUT RULES:
- Return exactly 3 bullet points.
- Do not provide an introduction.
- Do not provide a conclusion.
- Do not write anything before or after the 3 bullet points.
- Each bullet point must contain one concise explanation.

Return only the 3 bullet points.
"""

    print("\n========== STRICT OUTPUT ==========")
    print(ask_llama(prompt))


# --------------------------------------------------
# Experiment 2: Role Prompting
# --------------------------------------------------

def role_prompt_demo():
    prompt = """
You are an experienced customer support manager.

A customer says:

"My SIP trunk has been down for three hours and our business calls are failing."

Analyze the issue and recommend what the support team should do.
"""

    print("\n========== ROLE PROMPTING ==========")
    print(ask_llama(prompt))


# --------------------------------------------------
# Experiment 3: Intent Detection
# --------------------------------------------------

def intent_detection_demo():
    prompt = """
You are an intent classification system.

Classify the user's request into exactly one of these intents:

- schedule_meeting
- cancel_meeting
- check_schedule
- send_email
- other

User:
"Schedule a meeting with John tomorrow."

Return only the intent.
"""

    print("\n========== INTENT DETECTION ==========")
    print(ask_llama(prompt))


# --------------------------------------------------
# Experiment 4: Entity Extraction
# --------------------------------------------------

def entity_extraction_demo():
    prompt = """
You are an AI Business Operations Copilot.

Extract the meeting information from the user's request.

Identify:
- intent
- person
- date
- time

Return ONLY valid JSON.
Do not provide explanations.

User:
"Schedule a meeting with John tomorrow at 3 PM."
"""

    print("\n========== ENTITY EXTRACTION ==========")
    print(ask_llama(prompt))


# --------------------------------------------------
# Experiment 5: Intent + Entities
# --------------------------------------------------

def structured_output_demo():
    prompt = """
You are an AI Business Operations Copilot.

Analyze the user's request.

Return ONLY valid JSON with exactly these fields:

{
  "intent": "",
  "person": "",
  "date": "",
  "time": ""
}

User:
"Schedule a meeting with John tomorrow at 3 PM."

Do not provide explanations.
Do not use markdown.
Return only JSON.
"""

    print("\n========== STRUCTURED OUTPUT ==========")
    print(ask_llama(prompt))


# --------------------------------------------------
# Experiment 6: Classification
# --------------------------------------------------

def classification_demo():
    prompt = """
Classify the following support issue as exactly one of:

- low
- medium
- high
- critical

Customer:
"Our entire company's phone system is down and no employee can make or receive calls."

Return only the classification.
"""

    print("\n========== CLASSIFICATION ==========")
    print(ask_llama(prompt))


# --------------------------------------------------
# Experiment 7: Summarization
# --------------------------------------------------

def summarization_demo():
    prompt = """
Summarize the following customer conversation in exactly 3 bullet points.

Customer:
"Our SIP service stopped working at 10 AM today.
We restarted our router but the problem continues.
Around 30 employees are unable to make outbound calls.
We need this resolved as soon as possible."
"""

    print("\n========== SUMMARIZATION ==========")
    print(ask_llama(prompt))


# --------------------------------------------------
# Experiment 8: Planning
# --------------------------------------------------

def planning_demo():
    prompt = """
You are an AI Business Operations Copilot.

A customer reports that their SIP trunk is down
and business calls are failing.

Create a short action plan.

Return:

1. Identify the issue
2. Determine priority
3. First troubleshooting step
4. Escalation decision
5. Customer communication
"""

    print("\n========== PLANNING ==========")
    print(ask_llama(prompt))


# --------------------------------------------------
# Main
# --------------------------------------------------

if __name__ == "__main__":
    strict_output_demo()
    role_prompt_demo()
    intent_detection_demo()
    entity_extraction_demo()
    structured_output_demo()
    classification_demo()
    summarization_demo()
    planning_demo()