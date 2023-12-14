
word = input("Введите слово: ")

first_letter = word[0]
capitalized_word = chr(ord(first_letter) - ord('a') + ord('A')) + word[1:]

print("Слово с заглавной буквы:", capitalized_word)