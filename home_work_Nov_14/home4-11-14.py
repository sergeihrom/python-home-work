
coor_x1 =  input("Введите координату X1: ")
coor_x2 = input("Введите координату X2: ")
coor_y1 = input("Введите координату Y1: ")
coor_y2 = input("Ввеедите координату Y2: ")

x1 = float(coor_x1)
x2 = float(coor_x2)
y1 = float(coor_y1)
y2 = float(coor_y2)

distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


print("Расстояние между точками: ", distance )
