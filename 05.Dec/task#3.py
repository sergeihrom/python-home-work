
list1 = input("Введите элементы первого списка через пробел: ").split()
list2 = input("Введите элементы второго списка через пробел: ").split()

result_list = [x for x in list1 if x not in list2]

print("Список после удаления общих элементов:", result_list)