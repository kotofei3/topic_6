ALPHABETS = {
    "en_vowels": "AEIOU",
    "en_consonants": "BCDFGHJKLMNPQRSTVWXYZ",
    "ru_vowels": "АЕЁИОУЫЭЮЯ",
    "ru_consonants": "БВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬ",
}

print("Добро пожаловать в программу \"Буква-Детектив\"!", end="\n\n")

print("Выберите алфавит:\n"
      "1. Латинский\n"
      "2. Кириллица\n")

Enter_the_alphabet: str = input("Введите номер алфавита:")

if Enter_the_alphabet == "1":
    letter: str = input("Введите букву Латинский:")
    if letter in ALPHABETS["en_vowels"]:
        print(letter, "-", "гласная буква!")
    elif letter in ALPHABETS["en_consonants"]:
        print(letter, "-", "согласная буква")
    else:
        print("Упс! Неизвестная буква. Попробуйте другую!")
elif Enter_the_alphabet == "2":
    letter: str = input("Введите букву кириллицы:")
    if letter in ALPHABETS["ru_vowels"]:
        print(letter, "-", "гласная буква!")
    elif letter in ALPHABETS["ru_consonants"]:
        print(letter, "-", "согласная буква")
    else:
        print("Упс! Неизвестная буква. Попробуйте другую!")
