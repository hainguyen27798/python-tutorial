import math


def bernoulli(n: int, k: int, p: float) -> float:
  return math.comb(n, k) * p ** k * (1 - p) ** (n - k)


rs: int = 0

for i in range(3):
  rs += bernoulli(5, i, 0.2)

print(rs)
