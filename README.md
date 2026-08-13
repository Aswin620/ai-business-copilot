# AI Business Operations Copilot

An AI-powered business operations assistant designed to help
employees interact with company knowledge and perform
authorized business operations using natural language.

## Overview

The AI Business Operations Copilot combines a locally hosted
LLM, Retrieval-Augmented Generation (RAG), agent orchestration,
tool calling, conversational memory, human-in-the-loop approval,
and enterprise service integrations.

The project is being developed as a production-oriented
AI engineering project with a focus on security, evaluation,
observability, testing, and deployment.

## Example

A user can request:

> Schedule a meeting with the CEO tomorrow and update the
> sales sheet.

The system will:

1. Understand the request.
2. Determine the required operations.
3. Check relevant information.
4. Select appropriate tools.
5. Validate tool arguments.
6. Check user permissions.
7. Request approval when required.
8. Execute authorized operations.
9. Verify the results.
10. Return a response to the user.

## Architecture

```text
React + Tailwind
       │
       ▼
    FastAPI
       │
       ▼
   LangGraph
       │
   ┌───┴────┐
   ▼        ▼
Ollama     RAG
Llama      │
           ▼
      PostgreSQL
       + pgvector
           
       │
       ▼
     Tools
   ┌───┼────┐
   ▼   ▼    ▼
Calendar Gmail Sheets