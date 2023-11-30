user_01 = input("Введите дробное число: ")
user_02 =  input("Колличество знаков полсе запятой: ")

try:
    float_num = float(user_01)
    rounded_num = int(user_02)
except ValueError:
    print("Введите чило!")
else:
    roun_num2 = round(float_num, rounded_num)
    print(roun_num2)
