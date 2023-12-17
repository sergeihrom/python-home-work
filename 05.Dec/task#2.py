try:
    user_input = input("Введите числа через пробел: ")
    my_list = [int(x) for x in user_input.split()]
except ValueError:
    print("Введите числа цифрами!")
min_val = min(my_list)
max_val = max(my_list)

min_index = my_list.index(min_val)
max_index = my_list.index(max_val)

my_list[min_index], my_list[max_index] = my_list[max_index], my_list[min_index]

print("Список после обмена:", my_list)
