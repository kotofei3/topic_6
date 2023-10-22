number: int = int(input("Введите первое число: "))
number_2: int = int(input("Введите второе число: "))
operation: str = input("Введите магическую операцию:  ")

match operation:
    case "Призыв":
        result = number + number_2
        print(result)
    case "Трансформация":
        result = number - number_2
        print(result)
    case "Объединение":
        result = number * number_2
        print(result)
    case "Исчезновение":

        if number_2 == 0:
            print("Ошибка: Второе число равно нулю!")
        else:
            result = number / number_2
            print(result)
    case _:
        print("Ошибка: Некорректная операция")
