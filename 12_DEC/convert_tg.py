import re
import sys

# Заменяет суммы в долларах на тенге
def convert_to_tenge(match):
    amount = float(match.group(1))
    converted_amount = amount * usd_to_kzt_rate
    return f'{converted_amount:.2f} ₸'

# Заменяет суммы в евро на тенге
def convert_euro_to_tenge(match):
    amount = float(match.group(1))
    converted_amount = amount * euro_to_kzt_rate
    return f'{converted_amount:.2f} ₸'

# Проверка наличия аргументов командной строки
if len(sys.argv) != 3:
    print("Пожалуйста, укажите имена входного и выходного файлов.")
    sys.exit(1)

input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

# Текущие курсы валют (замените их соответственно)
usd_to_kzt_rate = 448.0
euro_to_kzt_rate = 510.0

try:
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        text = input_file.read()

    # Замена сумм в долларах
    text = re.sub(r'(\d+\.\d+) \$(?!\w)', convert_to_tenge, text)
    text = re.sub(r'(\d+\.\d+) USD(?!\w)', convert_to_tenge, text)

    # Замена сумм в евро
    text = re.sub(r'(\d+\.\d+) €(?!\w)', convert_euro_to_tenge, text)
    text = re.sub(r'(\d+\.\d+) EUR(?!\w)', convert_euro_to_tenge, text)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(text)

    print("Преобразование завершено. Результат записан в", output_file_path)

except FileNotFoundError:
    print("Файл не найден. Пожалуйста, укажите существующие файлы.")
except Exception as e:
    print("Произошла ошибка:", str(e))