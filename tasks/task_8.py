number: float = float(input("Введите первое число: "))
number_2: float = float(input("Введите второе число: "))
operation: str = input("Введите магическую операцию: ")

if operation == "Призыв":
    result = number + number_2
    print("Сумма магических сил чисел:", result)
elif operation == "Трансформация":
    result = number - number_2
    print("Трансформированное число:", result)
elif operation == "Объединение":
    result = number * number_2
    print("соединит числа,равна произведению чисел", result)
elif operation == "Исчезновение":
    if number_2 == 0:
        print("Ошибка: Второе число равно нулю!")
    else:
        print(number / number_2)
else:
    print("Ошибка: Некорректная операция")
