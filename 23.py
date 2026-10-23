n = int(input())
if n == 1:
    print(0)
else:
    n -= 2
    if n < 9:
        print(n + 1)
    else:
        n -= 9
        if n < 180:
            x = 10 + n // 2
            if n % 2 == 0:
                print(x // 10)
            else:
                print(x % 10)
        else:
            n -= 180
            x = 100 + n // 3
            if n % 3 == 0:
                print(x // 100)
            elif n % 3 == 1:
                print((x // 10) % 10)
            else:
                print(x % 10)