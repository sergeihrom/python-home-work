def format_text(text, max_line_length):
    paragraphs = text.split('\n\n')

    formatted_text = ""
    
    for paragraph in paragraphs:
        lines = paragraph.split('\n')
        formatted_paragraph = ""

        for line in lines:
            words = line.split()
            current_line = words[0].capitalize()

            for word in words[1:]:
                if len(current_line) + 1 + len(word) <= max_line_length:
                    current_line += " " + word
                else:
                    formatted_paragraph += current_line.ljust(max_line_length) + '\n'
                    current_line = word.capitalize()

            formatted_paragraph += current_line.ljust(max_line_length) + '\n'

        formatted_text += "    " + formatted_paragraph.rstrip() + "\n\n"

    return formatted_text.rstrip()

# Получаем текст и максимальную длину строки от пользователя
user_text = input("Введите текст: ")
max_length = int(input("Введите максимальную длину строки: "))

# Форматируем и выводим текст
formatted_result = format_text(user_text, max_length)
print(formatted_result)