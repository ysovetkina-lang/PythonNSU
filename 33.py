n = int(input())
c = int(input())
k = int(input())
p = (k - 1) // (n * c) + 1
r = (k - 1) % (n * c)
col = r // n + 1
row = r % n + 1
print(f"страница {p} столбец {col} строка {row}")