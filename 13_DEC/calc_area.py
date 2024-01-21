def calculate_area(length, width=None):
    try:
        if width is None:
            side = float(length)
            area = side ** 2
        else:
            length = float(length)
            width = float(width)
            area = length * width

        return area

    except ValueError:
        print("Ошибка: Введите корректные числовые значения.")

try:
    length_input = input("Введите длину прямоугольника (или сторону квадрата): ")

    width_input = input("Введите ширину прямоугольника (если необходимо): ")

    if width_input:
        result = calculate_area(length_input, width_input)
    else:
        result = calculate_area(length_input)

    print("Площадь:", result)

except Exception as e:
    print(f"Произошла ошибка: {str(e)}")