# System Architecture

## 1. Overview

The AI Business Operations Copilot follows a layered
architecture consisting of a presentation layer, API layer,
AI orchestration layer, tool integration layer, and data layer.

## 2. Frontend

React and Tailwind CSS will provide the user interface.

Responsibilities:

- User authentication
- Chat interface
- Streaming responses
- Approval requests
- Conversation history

## 3. Backend

FastAPI will provide the backend API.

Responsibilities:

- Authentication
- Request validation
- Conversation management
- Agent invocation
- Tool authorization
- Approval workflows
- API error handling

## 4. AI Orchestration

LangGraph will manage the agent workflow.

Responsibilities:

- Agent state
- Planning
- Tool selection
- Tool execution
- Conditional workflows
- Human approval

## 5. LLM

Ollama will provide local model inference.

The initial model will be Llama.

## 6. RAG

Company documents will be processed into chunks,
converted into embeddings, and stored in PostgreSQL
using pgvector.

## 7. Database

PostgreSQL will store persistent application data.

## 8. Cache

Redis will be used for temporary state, caching,
and asynchronous workloads.

## 9. External Integrations

The system will integrate with:

- Google Calendar
- Gmail
- Google Sheets