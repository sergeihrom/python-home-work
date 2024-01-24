from urllib.parse import urlparse, parse_qs

def parse_url_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()

    for url in urls:
        parsed_url = urlparse(url)
        
        print("Протокол:", parsed_url.scheme)
        print("Доменное имя:", parsed_url.netloc)
        print("Запрос:", parsed_url.path)

        query_params = parse_qs(parsed_url.query)
        if query_params:
            print("Параметры:")
            for key, values in query_params.items():
                for value in values:
                    print(f"   {key} = {value}")
        else:
            print("Параметры: отсутствуют")

        print()
        #VN: очень много побочных эффектов! Парсить должен парсить. А вывод информации делайте в основном коде, либо в другой функции

# Указываем путь к нашему текстовому файлу с URL
file_path = "my_file.txt"

parse_url_file(file_path)