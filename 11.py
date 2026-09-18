import math
a = float(input())
b = float(input())
r = max(a, b)
r2 = min(a, b)
print(math.pi * (r * r - r2 * r2))