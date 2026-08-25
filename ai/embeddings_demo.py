import torch


vocabulary = {
    "hello": 0,
    "business": 1,
    "copilot": 2,
    "ai": 3,
}

embedding_dimension = 4

embedding_table = torch.randn(
    len(vocabulary),
    embedding_dimension,
)

token = "business"

token_id = vocabulary[token]

embedding = embedding_table[token_id]

print("Token:")
print(token)

print("\nToken ID:")
print(token_id)

print("\nEmbedding:")
print(embedding)

print("\nEmbedding dimension:")
print(embedding.shape)