import torch


torch.manual_seed(42)

vocabulary = [
    "the",
    "business",
    "copilot",
    "is",
    "helpful",
]

logits = torch.randn(len(vocabulary))

probabilities = torch.softmax(logits, dim=0)

print("Token probabilities:\n")

for token, probability in zip(
    vocabulary,
    probabilities,
):
    print(
        f"{token:10} -> "
        f"{probability.item():.4f}"
    )

next_token_id = torch.argmax(probabilities)

print("\nSelected next token:")
print(vocabulary[next_token_id])