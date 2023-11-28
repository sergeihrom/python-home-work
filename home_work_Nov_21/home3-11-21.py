user_01 = input("Введите десятичное число: ")
try:
    num_01 = int(user_01)
except ValueError:
    print("Введитее число!")
else: 
     binary = bin(num_01)
     octal = oct(num_01)
     hexal = hex(num_01)
     
print(binary)
print(octal)
print(hexal)
