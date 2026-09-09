# System Architecture

## 1. Architecture Overview

The AI Business Operations Copilot follows a layered architecture.

The major layers are:

1. Presentation Layer
2. API Layer
3. Agent Orchestration Layer
4. AI/LLM Layer
5. Retrieval Layer
6. Tool Integration Layer
7. Data Layer
8. Observability Layer

The architecture is designed to keep AI reasoning separate from
security-sensitive business operations.

---

## 2. High-Level Architecture

```text
                         ┌─────────────────────┐
                         │       Employee      │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │    React Frontend   │
                         │    + Tailwind CSS   │
                         └──────────┬──────────┘
                                    │
                              HTTP / SSE
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │       FastAPI       │
                         │      Backend        │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      LangGraph      │
                         │   Agent Workflow    │
                         └──────┬──────┬───────┘
                                │      │
                     ┌──────────┘      └───────────┐
                     ▼                             ▼
              ┌──────────────┐              ┌──────────────┐
              │    Ollama    │              │     RAG      │
              │              │              │              │
              │ Llama Model  │              │  Embeddings  │
              └──────────────┘              └──────┬───────┘
                                                   │
                                                   ▼
                                            ┌──────────────┐
                                            │  PostgreSQL  │
                                            │  + pgvector  │
                                            └──────────────┘

                         Tool Integration Layer
                                  │
                ┌─────────────────┼─────────────────┐
                ▼                 ▼                 ▼
        Google Calendar        Gmail         Google Sheets


                         Supporting Services
                                  │
                    ┌─────────────┴─────────────┐
                    ▼                           ▼
                  Redis                    Langfuse
                 Caching                  Observability

## Local LLM Inference

The project uses Ollama as the local model runtime.

The current inference flow is:

React
  ↓
FastAPI
  ↓
Ollama
  ↓
Llama 3.1 8B

Ollama exposes a local HTTP API that allows the backend
to send prompts to the locally running Llama model.

Important inference parameters include:

- temperature
- top-p
- context
- streaming
- model selection


 


## Prompt Engineering and LLM Processing

The AI Business Operations Copilot uses prompt engineering
to convert natural-language user requests into structured
information that can be consumed by application logic.

The current local inference architecture is:

React
  ↓
FastAPI
  ↓
Ollama
  ↓
Llama 3.2 3B
  ↓
Structured LLM Response
  ↓
Application Logic


### Prompt Structure

A prompt can contain:

1. System/role instructions
2. Task instructions
3. Context
4. User input
5. Output format requirements


### Prompt Engineering Techniques

The project experiments with:

- Role prompting
- Zero-shot prompting
- Few-shot prompting
- Intent detection
- Classification
- Entity extraction
- Summarization
- Planning
- Structured output


### Intent Detection

Intent detection identifies what the user wants to accomplish.

Example:

User:

"Schedule a meeting with John tomorrow."

Result:

schedule_meeting


### Entity Extraction

Entity extraction identifies important information from
the user's request.

Example:

User:

"Schedule a meeting with John tomorrow at 3 PM."

Result:

{
  "person": "John",
  "date": "tomorrow",
  "time": "3 PM"
}


### Structured Output

LLMs normally generate natural-language responses.

For application integration, predictable structured output
is preferred.

Example:

{
  "intent": "schedule_meeting",
  "person": "John",
  "date": "tomorrow",
  "time": "3 PM"
}


Structured output allows application code to process
LLM results and eventually invoke business tools.


### Validation

LLM output should not be blindly trusted.

The intended processing flow is:

User Request
  ↓
LLM
  ↓
Structured Output
  ↓
Validation
  ↓
Business Logic
  ↓
Tool Execution


Validation will become increasingly important when the
system begins performing real business operations.


### Clarification

If required information is missing, the system should
request clarification instead of making assumptions.

Example:

User:

"Schedule something with John."

The system may identify:

{
  "intent": "schedule_meeting",
  "person": "John",
  "date": null,
  "time": null
}

The assistant should ask the user for the missing
date and time.


### Future Tool Calling

Prompt engineering provides the foundation for tool calling.

The intended future flow is:

User
  ↓
LLM
  ↓
Intent + Parameters
  ↓
Validation
  ↓
Tool Selection
  ↓
Tool Execution
  ↓
Tool Result
  ↓
LLM
  ↓
User
