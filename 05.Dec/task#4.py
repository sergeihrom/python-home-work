try:
    purchase_price = float(input("Введите стоимость покупки в $: "))
    discount_percentage = float(input("Введите размер скидки в %: "))
except ValueError:
    print("Введите данные цифрами!")
    exit()

discount_amount = purchase_price * (discount_percentage / 100)
total_amount = purchase_price - discount_amount


print(f"Стоимость покупки: ${purchase_price:.2f}")
print(f"Скидка: ${discount_amount:.2f} ({discount_percentage:.2f}%)")
print(f"Сумма к оплате: ${total_amount:.2f}")