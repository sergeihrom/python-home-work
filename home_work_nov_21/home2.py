try:
    user_input = input("Введите число: ")
    num = int(user_input)

    if num == 1:
        print("!")
    elif num == 2:
        print("@")
    elif num == 3:
        print("#")
    elif num == 4:
        print("$")
    elif num == 5:
        print("%")
    elif num == 6:
        print("^")
    elif num == 7:
        print("&")
    elif num == 8:
        print("*")
    elif num == 9:
        print("(")
    else:
        print("Некорректный ввод. Введите число от 0 до 9!")

except ValueError:
    print("Ошибка: Введите корректное число.")