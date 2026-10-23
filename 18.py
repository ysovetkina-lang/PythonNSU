a, b = map(float, input().split('*'))
c, d, e = map(float, input().split('*'))
minh = min(a, b)
maxh = max(a, b)
if (min(c, d) <= minh and max(c, d) <= maxh) or \
   (min(c, e) <= minh and max(c, e) <= maxh) or \
   (min(d, e) <= minh and max(d, e) <= maxh):
    print("Да")
else:
    print("Нет")