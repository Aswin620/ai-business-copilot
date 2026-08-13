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




 



