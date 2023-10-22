# year: int = int(input(": "))
# month: int = int(input(": "))
# month_nums: list = [1, 3, 5, 7, 8, 10, 12]
# result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
# if result and month in month_nums:
#     print("Да")
# else:
#     print("Нет")


year: int = int(input('Введите год: '))
month: int = int(input('Введите номер месяца: '))

n: list = [1, 3, 5, 7, 8, 10, 12]

match year, month:
    case _ if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 and month in n:
        print('Yes')
    case _:
        print('No')



