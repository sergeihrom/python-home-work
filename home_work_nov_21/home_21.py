try:
    user_input = input("Введите число: ")
    num = int(user_input)
except ValueError:
    print("Вы ввели не число!")
    exit()

hundreds = num // 100 % 10
tens = num // 10 % 10
ones = num % 10
if ones == tens or tens == hundreds or ones == hundreds:
    print("В числе есть одинаковые цифры")
else:
    print("В числе нет одинаковых цифр")

