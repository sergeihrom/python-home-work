user_01 = input("Введите значение a: ")
user_02 = input("Введите значение b: ")
try:
    a = int(user_01)
    b = int(user_02)
except ValueError:
    print("Ввдит значение в цифрах!")
else:   
    if a != 0:
        x = -b / a
        print(f'Значение х = {x}')
        print(a * x + b)
    else:
        print('a = 0')