try:
<<<<<<< HEAD
    user_input = input("Введите число: ")
    num = int(user_input)
=======
    num = int(user_01)
except ValueError:
    print("Вы ввели не число!")
#VN: в этой программе обработка исключения есть, но оно бесполезно. Программа падает, если ввести текст
hundreds = num // 100 % 10
tens = num // 10 % 10
ones = num % 10
if ones == tens or tens == hundreds or ones == hundreds:
    print("В числе есть одинаковые цифры")
else:
    print("В числе нет одинаковых цифр")
>>>>>>> 38b19571ae329c93151850440e9c4ce8d768b81d

    hundreds = num // 100 % 10
    tens = num // 10 % 10
    ones = num % 10

    if ones == tens or tens == hundreds or ones == hundreds:
        print("В числе есть одинаковые цифры")
    else:
        print("В числе нет одинаковых цифр")

except ValueError:
    print("Ошибка: Введите корректное целое число.")