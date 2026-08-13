# ADR-002: Use Ollama for Local LLM Inference

## Status

Accepted

## Date

2026-08-13

## Context

The AI Business Operations Copilot requires a language model
for natural-language understanding, structured outputs,
agent workflows, tool selection, and RAG-based responses.

During development, we want to run the model locally rather
than making the application dependent on a hosted LLM API.

The project also has a learning objective of understanding
LLM inference, model serving, and model customization rather
than only consuming an external API.

## Decision

We will use Ollama as the local LLM runtime during development.

The initial language model will be a Llama-family model.

The application will communicate with Ollama through its
local API.

The application will access Ollama through an abstraction
layer rather than spreading Ollama-specific implementation
throughout the codebase.

## Reasons

- Local model inference
- Simple model management
- Easy development workflow
- Local API access
- Suitable for experimentation
- Allows experimentation with different open models
- Supports the project's self-hosted LLM learning objective
- Allows future migration to another model-serving solution

## Consequences

### Positive

The development environment can run the LLM locally.

Sensitive development prompts and data do not need to be sent
to a hosted LLM provider.

The project team gains practical experience with model
inference and serving.

### Negative

Local inference requires sufficient CPU, RAM, and potentially
GPU resources.

Model performance may be lower than specialized cloud
infrastructure.

Larger models may require significant hardware resources.

## Future Consideration

For production deployment, the project may replace Ollama
with a dedicated model-serving infrastructure depending on
performance, scalability, and operational requirements.

The application should therefore avoid tightly coupling
business logic to the Ollama runtime.