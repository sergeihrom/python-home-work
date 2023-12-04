try:
    year_01 = input("Введите год: ")
    year = int(year_01)
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 !=0):
        print(year,"- год высокосный")
    else:
        print(year,"- не является высокосным")
except ValueError:
    print("Введите год числами!")   