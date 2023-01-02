import random

n = 12
v = random.choice(range(n))
A = random.choices(range(n), k=n)
print(f"{A=}")
print(f"{v=}")

for i, x in enumerate(A):
    # Loop invariant: if we've reached here, there's no value == v in A[:i].
    if x == v:
        print(i)
        break
else:  # nobreak
    print('nil')
