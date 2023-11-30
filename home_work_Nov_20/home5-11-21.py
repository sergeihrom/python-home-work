defoult_sales = 100
user_01 =input("Введите сумму продаж: ")

try:
    sales = int(user_01)
except ValueError:
    sales = defoult_sales
    print("Значение продаж выбранно по-молчанию.")
else:
    salary = sales * 0.1 + 250
    print("Ваша зарплата", salary,"$")
        