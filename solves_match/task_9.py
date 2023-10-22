number: int = int(input("Введите целое число: "))
number2: float = float(input("Введите дробное число: "))
line: str = input("Введите строку: ")

n: list = [number, number2, line]

match n:
    case _ if any(n):
        print('Yes')
    case _:
        print("No")
