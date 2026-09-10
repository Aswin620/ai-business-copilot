import json
from urllib.request import Request, urlopen

from pydantic import BaseModel


# --------------------------------------------------
# 1. Pydantic model
# --------------------------------------------------

class ScheduleMeetingRequest(BaseModel):
    attendees: list[str]
    date: str | None = None
    time: str | None = None
    duration: int = 30
    title: str | None = None
    
class MeetingProcessingResult(BaseModel):
    status: str
    meeting: ScheduleMeetingRequest
    missing: list[str] = []
    ambiguous: list[str] = []
    message: str


# --------------------------------------------------
# 2. Ollama configuration
# --------------------------------------------------

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"


# --------------------------------------------------
# 3. Send prompt to Llama
# --------------------------------------------------

def ask_llama(prompt: str) -> str:
    data = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "temperature": 0.1
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
# 4. Extract meeting information using Llama
# --------------------------------------------------

def extract_meeting_request(user_request: str):

    prompt = f"""
You are an information extraction system.

Extract meeting information from the user's request.

Return ONLY valid JSON.
Do not include markdown.
Do not include explanations.
Do not include any text before or after the JSON.

The JSON must contain exactly these fields:

{{
    "attendees": ["name"],
    "date": "date",
    "time": "time",
    "duration": 30,
    "title": "meeting title"
}}

Rules:

- attendees must be a list of names.
- date should contain the date information provided by the user.
- time should contain the time information provided by the user.
- duration must be an integer representing minutes.
- If duration is not provided, return null.
- If date, time, or title is not provided, return null.
- Do not invent missing information.

User request:
{user_request}
"""

    # Send request to Llama
    response = ask_llama(prompt)

    print("\nRaw Llama response:")
    print(response)

    # Convert JSON string → Python dictionary
    data = json.loads(response)

    # --------------------------------------------------
    # Normalize Llama output
    # --------------------------------------------------

    # Llama may return "null" as a string instead of JSON null.
    # Convert those strings into actual Python None values.
    for field in ["date", "time", "title"]:
        if data.get(field) == "null":
            data[field] = None

    # If duration is missing/null, use application default.
    if data.get("duration") is None:
        data["duration"] = 30

    # --------------------------------------------------
    # Pydantic validation
    # --------------------------------------------------

    meeting = ScheduleMeetingRequest(**data)

    return meeting


# --------------------------------------------------
# 5. Check for missing information
# --------------------------------------------------

def find_missing_information(meeting: ScheduleMeetingRequest):

    missing = []

    if not meeting.attendees:
        missing.append("attendees")

    if not meeting.date:
        missing.append("date")

    if not meeting.time:
        missing.append("time")

    return missing


# --------------------------------------------------
# 6. Check for ambiguous information
# --------------------------------------------------

def find_ambiguous_information(meeting: ScheduleMeetingRequest):

    ambiguous = []

    if meeting.date:
        date_value = meeting.date.lower()

        if date_value in [
            "soon",
            "later",
            "sometime",
            "next week"
        ]:
            ambiguous.append("date")

    if meeting.time:
        time_value = meeting.time.lower()

        if time_value in [
            "morning",
            "afternoon",
            "evening",
            "night",
            "later"
        ]:
            ambiguous.append("time")

    return ambiguous


# --------------------------------------------------
# 7. Generate clarification response
# --------------------------------------------------

def generate_clarification(missing, ambiguous):

    questions = []

    if "attendees" in missing:
        questions.append("Who should attend the meeting?")

    if "date" in missing:
        questions.append(
            "What date would you like to schedule the meeting?"
        )

    if "time" in missing:
        questions.append(
            "What time would you like to schedule the meeting?"
        )

    if "date" in ambiguous:
        questions.append(
            "Could you provide a more specific date?"
        )

    if "time" in ambiguous:
        questions.append(
            "Could you provide a specific time?"
        )

    if not questions:
        return "All required meeting information is available."

    return "\n".join(questions)


def process_meeting_request(user_request: str):
    
    # Step 1: Llama → JSON → Pydantic
    meeting = extract_meeting_request(user_request)

    # Step 2: Check missing information
    missing = find_missing_information(meeting)

    # Step 3: Check ambiguous information
    ambiguous = find_ambiguous_information(meeting)

    # Step 4: Decide what the application should do
    if missing or ambiguous:

        message = generate_clarification(
            missing,
            ambiguous
        )

        return MeetingProcessingResult(
            status="CLARIFICATION_REQUIRED",
            meeting=meeting,
            missing=missing,
            ambiguous=ambiguous,
            message=message
        )

    # Everything is available
    return MeetingProcessingResult(
        status="READY",
        meeting=meeting,
        missing=[],
        ambiguous=[],
        message="Meeting is ready for the next stage."
    )



def test_meeting_request(user_request: str):
    
    print("\n" + "=" * 60)
    print("TEST REQUEST:")
    print(user_request)
    print("=" * 60)

    try:

        result = process_meeting_request(user_request)

        print("\nFinal processing result:")
        print(result)

        print("\nStatus:")
        print(result.status)

        print("\nMeeting:")
        print(result.meeting)

        print("\nMissing:")
        print(result.missing)

        print("\nAmbiguous:")
        print(result.ambiguous)

        print("\nAssistant response:")
        print(result.message)

    except json.JSONDecodeError:

        print("\nERROR: Llama did not return valid JSON.")

    except Exception as error:

        print("\nERROR:", error)



# --------------------------------------------------
# 8. Main program
# --------------------------------------------------

if __name__ == "__main__":
    
    test_requests = [
        "Schedule a meeting with John tomorrow at 3 PM.",
        "Schedule a meeting with John tomorrow.",
        "Schedule a meeting with John.",
        "Schedule a meeting with John tomorrow afternoon.",
        "Schedule a meeting with John tomorrow evening for 60 minutes."
    ]

    for request in test_requests:
        test_meeting_request(request)