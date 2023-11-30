score = 0
score_step = 2

print("1. Самая высокая гора в мире: а)Кок-Жайлау, б) Эльбрус, в) Эврест.")
user_in = input ("Ваш отвт: ")
if user_in == "в":
    score += score_step
    print("верно")
else:
    print("неправильно")

print("2. Вккаком году Гагарин полетел в космос?: а)1976, б) 1961, в) 2001.")
user_in = input ("Ваш отвт: ")
if user_in == "б":
    score += score_step
    print("верно")
else:
    print("неправильно")

print("3. самаяя большая страна в мире: а)США, б) Китай, в) Россия.")
user_in = input ("Ваш отвт: ")
if user_in == "в":
    score += score_step
    print("верно")
else:
    print("неправильно")      

print("Вы держалисьь молодцом! и набрали ", score, "очков")  