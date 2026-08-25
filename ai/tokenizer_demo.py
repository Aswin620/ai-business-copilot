from transformers import AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained(
    "hf-internal-testing/llama-tokenizer"
)

text = "I love building AI applications."

tokens = tokenizer.tokenize(text)
token_ids = tokenizer.encode(text)

print("Original text:")
print(text)

print("\nTokens:")
print(tokens)

print("\nToken IDs:")
print(token_ids)

print("\nNumber of tokens:")
print(len(token_ids))