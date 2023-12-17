try:
    user_input = input("Введите числа через пробел: ")
    my_list = [int(x) for x in user_input.split()]
except ValueError:
    print("Введите числа цифрами!")
    exit()

result_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(result_list)