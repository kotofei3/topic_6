if (number := int(input('Введите целое число:'))) % 2 == 0:
    print('Число', number, 'является четным')
elif number % 2 == 1:
    composition = number * 3
    if composition > 20:
        print('Результат умножения', number, 'на', 3, 'больше', 20)
    else:
        print('Число', number, 'не соответствует условиям')

# -------------------------------

if (number := int(input('Введите целое число:'))) % 2 == 0:
    print('Число', number, 'является четным')
elif (number * 3) > 20:
    print('Результат умножения', number, 'на', 3, 'больше', 20)
else:
    print('Число', number, 'не соответствует условиям')
