stocking_number: int = int(input('Введите целое число: '))

if stocking_number > 0:
    print(1)
elif stocking_number < 0:
    print(-1)
else:
    print(0)

# -------------------- №2

number: int = int(input('Введите целое число:'))
condition = '1' if number > 0 else '-1'
print(condition)
