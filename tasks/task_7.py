number: int = int(input("Введите целое число: "))
number_2: float = float(input("Введите дробное число:"))
line: str = input("Введите строку:")

# Подсказка к 7 и 9 задачке:
# Тема №5
# Встроенные функции Python: для работы с коллекциями и числами

if all([number, number_2, line]):
    print('Да')
else:
    print('Нет')
