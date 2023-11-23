user_01 =input("трехзначное число: ")

number = int(user_01)

if 100 <= number <= 999:
    second_digit = (number // 10) % 10
    print("Вторая цифра числа", second_digit)
else:
    print("Число не является трехзначным.")