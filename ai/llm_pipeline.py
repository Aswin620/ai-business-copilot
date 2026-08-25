def explain_llm_pipeline():
    pipeline = [
        "1. User provides text",
        "2. Tokenizer converts text into tokens",
        "3. Tokens are converted into token IDs",
        "4. Token IDs are mapped to embeddings",
        "5. Positional information is added",
        "6. Transformer processes the representations",
        "7. Self-attention determines token relationships",
        "8. Feed-forward networks transform representations",
        "9. Residual connections preserve information flow",
        "10. Layer normalization stabilizes representations",
        "11. Final representation is projected into logits",
        "12. Softmax converts logits into probabilities",
        "13. A next token is selected",
        "14. The process repeats until generation stops",
    ]

    for step in pipeline:
        print(step)


if __name__ == "__main__":
    explain_llm_pipeline()