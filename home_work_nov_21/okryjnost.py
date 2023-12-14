
try:
    Us_C = input("Введите длину окружности: ")
    Us_P = input("Введите периметр квадрата: ")

    circle = float(Us_C)
    perimeter = float(Us_P)
except ValueError:
    print("Введите цифры!")
    exit()

length_square = perimeter / 4

if circle <= length_square:
    print("Данная окружность помещается в квадрат.")
else:
    print("Данная окружность не помещается в квадрат.")
