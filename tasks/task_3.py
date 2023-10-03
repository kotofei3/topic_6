age: int = int(input('Введите свой возраст: '))

leve: str = 'Вы находитесь на уровне \"Инициации\" '
leve_2: str = 'Вы находитесь на уровне \"Приключений\" '
level_3: str = 'Вы находитесь на уровне \"Мудрости\"'
level_4: str = 'Вы находитесь на уровне \"Мастерства\"'

# if age > 0 and age < 18:
if 0 < age < 18:
    print(leve)
elif age >= 18 and age <= 30:
    print(leve_2)
elif age >= 31 and age <= 50:
    print(level_4)
elif age >= 51 and age <= 65:
    print(level_3)
else:
    if age > 65:
        print('Вы находитесь на уровне \"Легенд\"')
    else:
        print('Возраст должен быть больше 0')
