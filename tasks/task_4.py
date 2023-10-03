number_1: int = int(input('Введите первое целое число:'))
number_2: int = int(input('Введите второе целое число:'))
number_3: int = int(input('Введите третье целое число:'))

if number_1 > number_2:
    maximum = number_1
    print('Наибольшее число:', maximum)
else:
    maximum = number_2
    print('Наибольшее число:', maximum)
if number_3 > maximum:
    maximum = number_3
    print('Наибольшее число:', maximum)
else:
    if number_1 == number_2 == number_3:
        print('Все числа равны')


# a = 2
# b = 4
# c = 9
# if a > b:
#     print(a)
# elif a < b:
#     print(b)
# elif b > a:
#     print(b)
# elif b < a:
#     print(a)
# elif c > a:
#     print(c)
# elif c < a:
#     print(a)
# elif c > b:
#     print(c)
# elif c < b:
#     print(b)
# else:
#     print('=')

