old: int = int(input("Введите свой возраст: "))
maze = ""
match old:
    case _ if 0 < old < 18:
        maze = "Инициации"
    case _ if 18 <= old <= 30:
        maze = "Приключений"
    case _ if 31 <= old <= 50:
        maze = "Мастерства"
    case _ if 51 <= old <= 65:
        maze = "Мудрости"
    case _ if old > 65:
        maze = "Легенд"
    case _:
        maze = "NO"
print(maze)
