while True:
    n = int(input("Введите число: "))
    i = 1
    found = False
    while i * i <= n:
        if i * i == n:
            found = True
            break
        i += 1
    if found:
        print(f"Вы молодец, введенное число является полным квадратом {i}")
        break
    else:
        print("Введенное Вами число не является полным квадратом, введите другое")