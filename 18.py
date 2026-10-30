x = int(input())
c = 0
for a in range(1, int(x ** 0.5) + 1):
    b2 = x - a * a
    b = int(b2 ** 0.5)
    if b * b == b2 and a <= b:
        c += 1
print(c)