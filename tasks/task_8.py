number: int = int(input(":"))
number_2: int = int(input(":"))
a_call: str = input(":")

if a_call == "Призыв":
    result = number + number_2
    print('Сумма магических сил чисел:', float(result))
elif a_call == "Трансформация":
    result = number + number_2
    print('Трансформированное число',float(result))
elif a_call == "Исчезновение":
    result = number - number
    if number_2 == 0:
        print("Ошибка: Второе число равно нулю!",)
    else:
        print(result)
