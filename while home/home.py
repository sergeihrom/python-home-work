# Запросить у пользователя 10 чисел и подсчитать, сколько он ввел положительных, отрицательных и нулей. При этом также посчитать, сколько четных и нечетных. Вывести статистику на экран. 
# Важно! Учтите, что достаточно одной переменной (не 10) и одного input() для ввода чисел пользователем.

count_positive = 0
count_negative = 0
count_zero = 0
count_even = 0
count_odd = 0

# Счетчик ввода чисел
counter = 0

while counter < 10:
    number = float(input("Введите число: "))
    
    # Определение типа числа и обновление счетчиков:
    if number > 0:
        count_positive += 1
    elif number < 0:
        count_negative += 1
    # Определеение четности числа:
    else:
        count_zero += 1
    if number % 2 == 0:
        count_even += 1
    else:
        count_odd += 1 
    counter += 1

print("Положительных чисел: ", count_positive)
print("Отрицательных чисел:", count_negative)
print("Нулей: ", count_zero)
print("Четных чисел:", count_even)
print("Нечетных чисеел:", count_odd)