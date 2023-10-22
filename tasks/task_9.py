number: int = int(input("Введите целое число: "))
number_2: float = float(input("Введите дробное число: "))
line: str = input("Введите строку: ")

listing: list = [number, number_2, line]

if any(listing) == True:
    print("Да")
else:
    print("Нет")
