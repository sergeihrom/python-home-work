
word = input("Введите слово: ")

#VN: тут важно сделать проверку длины слова, иначе 'me' сокращается как 'me-me'
abbreviation = word[:2] + "-" + word[-2:]

print(f"Слово: {word} сокращается как: {abbreviation}")