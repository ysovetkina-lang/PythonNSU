x, y, n = map(int, input().split())
t = (x * 100 + y) * n
print(f"{t // 100} руб. {t % 100} коп.")