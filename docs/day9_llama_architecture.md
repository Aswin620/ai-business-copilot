# Day 9 — Llama Architecture

## Architecture

Tokenizer
→ Embeddings
→ Transformer Blocks
→ Attention
→ MLP
→ Output Head
→ Logits
→ Sampling
→ Next Token

## Parameters

Learned numerical values inside the model.

## Weights

Learned parameters used by neural network layers.

## Context Window

Maximum token context available to the model.

## Inference

Using a trained model to generate predictions.

## Temperature

Controls randomness during sampling.

## Top-p

Controls the probability mass considered during sampling.

## Quantization

Reducing numerical precision to reduce model size
and resource requirements.

## Local Architecture

FastAPI
→ Model Client
→ Ollama
→ Llama

## Key Learning

The application does not need to directly communicate
with a cloud LLM API. A local model server can expose
the model through an HTTP interface.