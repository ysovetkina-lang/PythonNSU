xc = float(input())
yc = float(input())
r = float(input())
x = float(input())
y = float(input())
d = (x - xc)**2 + (y - yc)**2
r2 = r**2
if d < r2:
    print("Точка внутри окружности")
elif d == r2:
    print("Точка на окружности")
else:
    print("Точка вне окружности")
