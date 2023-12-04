
try:
    Us_C = input("Введите длину окружности: ")
    Us_P = input("Введите периметр квадрата: ")

    circle = float(Us_C)
    perimeter = float(Us_P)

    length_square = perimeter / 4

    # Если длина окружности меньше или равна половине периметра квадрата, то круг помещается в квадрат
    if circle <= length_square:
        print("Данная окружность помещается в квадрат.")
    else:
        print("Данная окружность не помещается в квадрат.")
except ValueError:
    print("Введите цифры!")