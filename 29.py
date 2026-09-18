import math
x = float(input())
y = float(input())
z = float(input())
print(math.degrees(math.acos((y * y + z * z - x * x) / (2 * y * z))))
print(math.degrees(math.acos((x * x + z * z - y * y) / (2 * x * z))))
print(math.degrees(math.acos((x * x + y * y - z * z) / (2 * x * y))))