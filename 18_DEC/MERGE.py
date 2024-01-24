def merge_digits():
    #VN: функция должна принимать три числа в качестве аргументов. Задача не решена
    # + те же замечания, что и к остальным задачам
    try:
        digit1 = int(input("Введите первую цифру: "))
        digit2 = int(input("Введите вторую цифру: "))
        digit3 = int(input("Введите третью цифру: "))

        combined_number = int(f"{digit1}{digit2}{digit3}")
        return combined_number

    except ValueError:
        print("Ошибка: Введите три цифры!")


try:
    result = merge_digits()
    print(result)
except Exception as e:
    print(f"Произошла ошибка: {str(e)}")
