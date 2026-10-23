n = int(input())

# 1 г = 17 с * 29 к = 493 кната
g = n // 493
n = n % 493

# 1 с = 29 к
s = n // 29
k = n % 29

if g > 0:
    print(g, "галлеонов")
if s > 0:
    print(s, "сиклей")
if k > 0:
    print(k, "кнатов")