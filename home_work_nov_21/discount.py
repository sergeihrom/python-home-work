
try:
    user_input = input("Введите сумму покупки: ")
    summ = int(user_input)

    if 200 <= summ < 300:
        discount_price = summ - (summ * 3 / 100)
        print("Ваша сумма со скидкой: ", discount_price)
    elif 300 <= summ < 500:
        discount_price = summ - (summ * 5 / 100)
        print("Ваша сумма со скидкой: ", discount_price)
    else:
        discount_price = summ - (summ * 7 / 100)
        print("Ваша сумма со скидкой: ", discount_price)

except ValueError:
    print("Ошибка: Введите корректное значение для суммы покупки.")