
eur = 0.92
uan= 7.09
azn = 1.70

try:
   User_in = input("Ввдите колличеество USD: ")
   summ = float(User_in)
except  ValueError:
   print("Введите сумму цифрами!")
   exit()

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

    

    
    






