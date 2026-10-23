pin = input()
if len(pin) == 4 and pin.isdigit():
    n = int(pin)
    d1 = n // 1000
    d2 = (n // 100) % 10
    d3 = (n // 10) % 10
    d4 = n % 10
    if d1 != d2 and d1 != d3 and d1 != d4 and d2 != d3 and d2 != d4 and d3 != d4:
        if 1900 <= n <= 2050:
            print("ERROR")
        else:
            print("OK")
    else:
        print("ERROR")
else:
    print("ERROR")