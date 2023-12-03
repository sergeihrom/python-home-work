user_in = input("Введите сумму покупки: ")
summ = int(user_in)
#VN: нет обработки исключения!
if 200 <= summ < 300:
    discountPrice = (summ - (summ * 3 / 100))
    print("Ваша сумма со скидкой: ", discountPrice)
elif 300 <= summ < 500:
    discountPrice = (summ - (summ * 5 / 100))
    print("Ваша сумма со скидкой: ", discountPrice)
else:
    discountPrice = (summ - (summ * 7 / 100))
    print("Ваша сумма со скидкой: ", discountPrice)
