
user_day = input("Введите дневную температуру: ")
user_night = input("Ввеедите ночную температуру: ")

try:
    daytime = int(user_day)
    night = int(user_night)
except ValueError:
    print("Вы ввели не число!")   
else:
     difference = abs(daytime - night)
     print("Разница темпратуры: ", difference)
