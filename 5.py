a, b, c = map(int, input().split())
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

    #или

a, b, c = map(int, input().split())
best = a
if b > best:
    best = b
if c > best:
    best = c
print(best)