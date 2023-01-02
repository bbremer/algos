"""Input: Two sequences of n bits A = <a_1, ..., a_n> and B = <b_1, ..., b_n>.
Output: A sequence of n+1 bits C = <c_1, ..., c_n, c_{n+1}."""

import random

n = 10
A = random.choices((0, 1), k=10)
B = random.choices((0, 1), k=10)
print(f"{A=}")
print(f"{B=}")

carry = 0
C = []
for a, b in zip(A, B):
    c = a + b + carry
    if c < 2:
        carry = 0
        C.append(c)
    else:
        carry = 1
        C.append(0)
C.append(carry)

print(f"{C=}")

print(f"{int(''.join(str(a) for a in A[::-1]), 2)} + "
      f"{int(''.join(str(b) for b in B[::-1]), 2)} = "
      f"{int(''.join(str(c) for c in C[::-1]), 2)}")

print(f"{sum(a * 2**i for i, a in enumerate(A))} + "
      f"{sum(b * 2**i for i, b in enumerate(B))} = "
      f"{sum(c * 2**i for i, c in enumerate(C))}")
