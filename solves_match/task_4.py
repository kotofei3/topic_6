a: int = int(input("Введите первое целое число: "))
b: int = int(input("Введите второе целое число: "))
c: int = int(input("Введите третье целое число: "))

match a, b, c:
    case _ if a > b and a > c:
        print('Наибольшее число', a, sep=':')
    case _ if b > c:
        print('Наибольшее число', b, sep=':')
    case _ if c > b:
        print('Наибольшее число', c, sep=':')
    case _:
        print('Все числа равны')
