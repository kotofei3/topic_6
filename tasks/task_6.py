year: int = int(input(":"))
month: int = int(input(":"))
if year % 4 == 0:
    if month > 11:
        print('YES')
    else:
        print('NO')
