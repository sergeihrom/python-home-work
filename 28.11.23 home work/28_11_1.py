try:
    user_in = input("ввдите число!")
    num = int(user_in)
    for i in range (1, num+1):
        if num % i == 0:
            print(i)
except ValueError:
    print("Ввдите число цифрами!")