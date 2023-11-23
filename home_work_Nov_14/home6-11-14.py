user_01 = input("Введите значение a: ")
user_02 = input("Введите значение b: ")

a = int(user_01)
b = int(user_02)

if a != 0:
    x = -b / a
    print(f'Значение х = {x}')
    print(a * x + b)
else:
    print('a = 0')