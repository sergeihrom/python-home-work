# Запросить у пользователя длину окружности и периметр квадрата. Определить, может ли такая окружность поместиться в указанный квадрат. 
Us_C = input("Введите длину окружности: ")
Us_P = input("Введите перриметр квадрата: ")

circle = float(Us_C)
perimeter = float(Us_P)

length_square = perimeter / 4 
# если длина окружности == длине квадрата или < длины квадрата то круг поместиться в квадрат !
if length_square == circle or length_square > circle:
    print("Данная окруужность помещается в квадрат.")
else:
    print("данная окружность не помещается в квадрат!")