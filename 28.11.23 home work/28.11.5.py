# Запросить у пользователя число и вывести наибольшую цифру из этого числа и наименьшую.

number = input("Введите число: ")

max_digit = float('-inf')
min_digit = float('inf')

index = 0

while index < len(number):
    current_digit = int(number[index])
    
    if current_digit > max_digit:
        max_digit = current_digit
    
    if current_digit < min_digit:
        min_digit = current_digit
    
    index += 1

print(f"Наибольшая цифра: {max_digit}")
print(f"Наименьшая цифра: {min_digit}")
