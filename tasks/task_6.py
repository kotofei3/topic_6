year: int = int(input('Введите год: '))
month: int = int(input('Введите номер месяца: '))
number: tuple = (1, 3, 5, 7, 8, 10, 12)

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    if month in number:
        print('Да')
    else:
        print('Нет')
else:
    print('Нет')
