user_01 =input("трехзначное число: ")
try:
    number = int(user_01)
except ValueError:
    print("Вы ввеели не число!")
else:

    if 100 <= number <= 999:
        second_digit = (number // 10) % 10
        print("Вторая цифра числа", second_digit)
    else:
        print("Число не является трехзначным.")