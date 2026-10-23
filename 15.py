n, k, m = map(int, input().split())
d = abs(k - m)
a = d - 1
b = n - d - 1
if a < b:
    print(a)
else:
    print(b)