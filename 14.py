while True:
    s = input("Введите число: ")
    if s.isdigit():
        print(f"Введено целое число: {s}")
        break
    else:
        print("Ошибка. Попробуйте еще раз.", end=" ")