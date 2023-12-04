# Написать конвертор валют. Пользователь вводит количество USD, выбирает, в какую валюту хочет перевести: EUR, UAN или AZN, и получает в ответ соответствующую сумму, или сообщение о том, что такая валюта недоступна, если он выбрал что-то другое.
<<<<<<< HEAD
try:
   eur = 0.92
   uan= 7.09
   azn = 1.70
   User_in = input("Ввдите колличеество USD: ")
   summ = float(User_in)
   print("Введите нужную валюту:(eur, uan, azn)")
   currency = input("Ваша валюта: ")
   if currency == "eur":
      convertacia = eur * summ
      print("Ваша сумма в EUR:", convertacia)
   elif currency == "uan":
      convertacia = uan * summ
      print("Ваша сумма в UAN:", convertacia)
   elif currency == "azn":
      convertacia = azn * summ
      print("Ваша сумма в AZN:", convertacia)
   else:
      print("Выберете валюту!")
except ValueError:
   print("Введит сумму в цифрах")
=======

eur = 0.92
uan= 7.09
azn = 1.70
User_in = input("Ввдите колличеество USD: ")
summ = float(User_in)
#VN:   ^^^^^^ нет обработки исключения!
print("Введите нужную валюту:(eur, uan, azn)")
currency = input("Ваша валюта: ")
if currency == "eur":
   convertacia = eur * sum
   #VN:                ^^^ опечатка. Если ввести 'eur', программа здесь падает. 
   print("Ваша сумма в EUR:", convertacia)
elif currency == "uan":
   convertacia = uan * summ
   print("Ваша сумма в UAN:", convertacia)
elif currency == "azn":
   convertacia = azn * summ
   print("Ваша сумма в AZN:", convertacia)
else:
    print("Выберете валюту!")
>>>>>>> 38b19571ae329c93151850440e9c4ce8d768b81d
    

    
    






# user_in = input ("Ваш отвт: ")
# if user_in == "в":
#     score += score_step
#     print("верно")
# else:
#     print("неправильно")