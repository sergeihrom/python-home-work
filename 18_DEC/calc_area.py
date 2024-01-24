def calculate_area(length, width=None):
    try:
        if width is None:
            side = float(length)
            #VN:   ^^^^^^^^^^^^ лишнее преобразование
            area = side ** 2
        else:
            length = float(length)
            width = float(width)
            #VN:   ^^^^^^^^^^^^ лишние преобразования
            area = length * width

        return area

    except ValueError:
        print("Ошибка: Введите корректные числовые значения.")

    #VN: функция не должна заниматься преобразованием данных, если только это не прямое назначение функции
    # print в функции тоже не нужен - это побочный эффект.

try:
    #VN: но если в вашей функции есть блок try, то зачем ещё один?
    length_input = input("Введите длину прямоугольника (или сторону квадрата): ")

    width_input = input("Введите ширину прямоугольника (если необходимо): ")
    #VN: input незачем помещать в try!

    if width_input:
        result = calculate_area(length_input, width_input)
    else:
        result = calculate_area(length_input)

    print("Площадь:", result)
    #VN: print какое искличение может вызвать? зачем он в try?

except Exception as e:
    #VN: ^^^^^^^^ какое именно исключение ожидаете?
    print(f"Произошла ошибка: {str(e)}")


#VN: помещать весь алгоритм в try недопустимо!