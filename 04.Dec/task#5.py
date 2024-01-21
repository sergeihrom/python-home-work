try:
    n = int(input("Введите длину строки: "))
    #VN: разделяёте операции ввода данных и их преобразования! input'ам не место в try
except ValueError:
    print("Введите значение в цифрах!")
    exit()
c1 = input("Введите первый символ (C1): ")
c2 = input("Введите второй символ (C2): ")


result_string = (c1 + c2) * (n // 2) + c1 * (n % 2)


print("Созданная строка:", result_string)