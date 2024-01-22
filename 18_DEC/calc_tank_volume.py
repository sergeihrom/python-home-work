def calculate_tank_volume(diameter, height):
    try:
        diameter = float(diameter)
        height = float(height)

        radius = diameter / 2
        volume_liters = 3.14159 * radius ** 2 * height * 1000 
        return volume_liters

    except ValueError:
        print("Ошибка: Введите корректные числовые значения.")

try:
    diameter_input = input("Введите диаметр бака (в метрах): ")
    height_input = input("Введите высоту бака (в метрах): ")

    result = calculate_tank_volume(diameter_input, height_input)

    print(f"Объем бака: {result:.2f} литров")

except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
