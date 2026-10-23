s = input()
n, m = map(int, s.split('x'))
k = int(input())
if (k % n == 0 and k // n < m) or (k % m == 0 and k // m < n):
    print("возможно")
else:
    print("невозможно")