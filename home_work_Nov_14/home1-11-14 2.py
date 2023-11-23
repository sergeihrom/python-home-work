
user_day = input("Введите дневную температуру: ")
user_night = input("Ввеедите ночную температуру: ")

daytime = int(user_day)

night = int(user_night)

difference = abs(daytime - night)

print("Разница темпратуры: ", difference)
