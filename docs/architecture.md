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


 



