user_01 = input("Введите слово: ")

if len(user_01) != 5:
    print("Введите слово из 5 букв!")
elif user_01 == user_01 [::-1]:
    print("Слово являтся палиндромом!")
else:
    print("Не является палиндромом!")

