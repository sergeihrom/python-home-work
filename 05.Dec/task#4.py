# Ввод массива от пользователя c обработкой исключения ValueError
try:
    array = input("Введите числа массива через пробел: ").split()
    #VN: ^^^^^^^^ эта строка не нужна в try
    array = [int(x) for x in array]
except ValueError:
    print("Введите значения цифрами!")
# Находим индексы минимального и максимального чисел
min_index = array.index(min(array))
max_index = array.index(max(array))

# Вычисляем расстояние между минимальным и максимальным числами
distance = abs(min_index - max_index)

print("Расстояние между минимальным и максимальным числами:", distance)

#VN: программа работает неправильно, если пользователь ввёл где-то не число