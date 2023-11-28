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

    remaining_hh = remaining_mm // 60
    remaining_mm %= 60

    print(f"До следующего дня осталось {remaining_hh} часов и {remaining_mm} минут.")