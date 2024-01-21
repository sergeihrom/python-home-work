try:
    user_input = input("Введите числа через пробел: ")
    #VN: ^^^^^^^^ эта строка не нужна в try
    my_list = [int(x) for x in user_input.split()]
except ValueError:
    print("Введите числа цифрами!")
    exit()

result_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
#VN: достаточно сложно читается такая конструкция, но лично мне нравится)
print(result_list)