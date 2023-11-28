user_01 = input('hh: ')
user_02 = input('mm: ')
try:
    hh = int(user_01)
    mm = int(user_02)
except ValueError:
    print("Ввеедите часы и минуты!")
else:

    passed_mm = hh * 60 + mm

    remaining_mm = 1440 - passed_mm

<<<<<<< HEAD
    remaining_hh = remaining_mm // 60
    remaining_mm %= 60
=======
remaining_mm = 1440 - passed_mm
#VN: значение  ^^^^ не очевидно относится к предметной области, и в коде такие числа всегда вызывают вопросы
# лучше всего эту строку было бы написать так: remaining_mm = 24 * 60 - passed_mm. Тогда при чтении сразу
# понятно, о чём идёт речь и что это за значения. А Python при запуске такие явные вычисления делает заранее и
# производительность от этого не страдает.
>>>>>>> 56b7ebc9aa740a345fec35adb00b91b8867a2938

    print(f"До следующего дня осталось {remaining_hh} часов и {remaining_mm} минут.")