try:
    user_input = input("Введите число: ")
    num = int(user_input)
except ValueError:
    print("Введите значение цифрами!")
    exit()
    
match num:
    case 1:
        print('!')
    case 2:
        print('@')
    case 3:
        print('#')
    case 4:
        print('$')
    case 5:
        print('%')
    case 6:
        print('^')
    case 7:
        print('&')
    case 8:
        print('*')
    case 9:
        print('(')
   



