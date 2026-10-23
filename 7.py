n = int(input())
d1 = n // 1000
d4 = n % 10
d2 = (n - d1*1000) // 100
d3 = (n // 10) % 10
if d1 == d4 and d2 == d3:
    print("настоящее")
else:
    print("кривое")