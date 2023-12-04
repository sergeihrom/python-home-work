# 1. Пользователь вводит два числа - начало и конец диапазона. Подсчитать сумму всех чисел в этом диапазоне.

start = int(input("Ввдите число: "))
end = int(input("Ввдите конец диапазона:"))
sum = 0
currant = start
while currant <= end:
    sum += currant
    currant += 1
print(sum)

