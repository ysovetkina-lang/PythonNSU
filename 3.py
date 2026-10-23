print("Вы поедете на бал?")
answer = input("Ответ: ")
if not (answer.lower().strip() == "да" or answer.lower().strip() == "нет"):
    print("Верно")
else:
    print("Неверно")