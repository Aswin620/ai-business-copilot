import math

import torch


torch.manual_seed(42)

sequence_length = 4
embedding_dimension = 8

x = torch.randn(
    sequence_length,
    embedding_dimension,
)

W_q = torch.randn(
    embedding_dimension,
    embedding_dimension,
)

W_k = torch.randn(
    embedding_dimension,
    embedding_dimension,
)

W_v = torch.randn(
    embedding_dimension,
    embedding_dimension,
)

Q = x @ W_q
K = x @ W_k
V = x @ W_v

scores = Q @ K.T

scaled_scores = scores / math.sqrt(
    embedding_dimension
)

attention_weights = torch.softmax(
    scaled_scores,
    dim=-1,
)

output = attention_weights @ V

print("Input shape:")
print(x.shape)

print("\nAttention weights:")
print(attention_weights)

print("\nAttention output shape:")
print(output.shape)