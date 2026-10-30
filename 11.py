x = int(input())
best = x
while x != -1:
    if x > best:
        best = x
    x = int(input())
print(best)