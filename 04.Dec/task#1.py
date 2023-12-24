
try:
    year = int(input("Введите год вашего рождения: "))
    month = int(input("Введите месяц вашего рождения: "))
    day = int(input("Введите число вашего рождения: "))
    #VN: разделяёте операции ввода данных и их преобразования! input'ам не место в try
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите числа.")
else:
    formatted_date = "{:02d}.{:02d}.{}".format(day, month, year)
    print("Дата вашего рождения: ", formatted_date)