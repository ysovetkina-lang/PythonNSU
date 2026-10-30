n = int(input())
for i in range(2, n + 1):
    p = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            p = False
            break
    if p:
        print(i, end=" ")