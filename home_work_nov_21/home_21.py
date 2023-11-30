
user_01 = input("Ввеедит трехзначное число: ")
try:
    num = int(user_01)
except ValueError:
    print("Вы ввели не число!")
hundreds = num // 100 % 10
tens = num // 10 % 10
ones = num % 10
if ones == tens or tens == hundreds or ones == hundreds:
    print("В числе есть одинаковые цифры")
else:
    print("В числе нет одинаковых цифр")

