import random

A = random.choices(range(100), k=10)
print(A)

for i in range(len(A)-1):
    min_j = min(range(i, len(A)), key=lambda x: A[x])
    A[i], A[min_j] = A[min_j], A[i]

print(A)
