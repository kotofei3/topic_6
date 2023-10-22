number: int = int(input("Введите целое число: "))
number_2: float = float(input("Введите дробное число: "))
line: str = input("Введите строку: ")

listing: list = [number, number_2, line]

if any(listing):
    print("Да")
else:
    print("Нет")

# a: list = [1]
# b: tuple = ('1',)
#
# match any(a), any(b):
#     case True,True:
#         print(True)
#     case _:
#         print(False)
