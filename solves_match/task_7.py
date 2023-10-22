figure: int = int(input("Введите целое число: "))
number: float = float(input("Введите дробное число: "))
line: str = input("Введите строку:  ")

match all((figure, number, line)):
    case True:
        print("Да")
    case _:
        print("Нет")
