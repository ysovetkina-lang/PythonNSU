t1 = float(input())
c = 0
t2 = float(input())
while t2 != 0:
    if t2 < t1:
        c += 1
    t1 = t2
    t2 = float(input())
print(c)