s1, s2 = input().split()
x1 = "abcdefgh".find(s1[0]) + 1
y1 = int(s1[1])
x2 = "abcdefgh".find(s2[0]) + 1
y2 = int(s2[1])

dx = abs(x1 - x2)
dy = abs(y1 - y2)

if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print("верно")
else:
    print("ошибка")