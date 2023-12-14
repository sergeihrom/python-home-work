
word = input("Введите слово: ")

abbreviation = word[:2] + "-" + word[-2:]

print(f"Слово: {word} сокращается как: {abbreviation}")