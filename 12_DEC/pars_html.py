import html.parser
import sys
from html import unescape

class HTMLParser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_title = False
        self.in_header = False

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.in_title = True
        elif tag.startswith('h') and tag[1:].isdigit():
            self.in_header = True

    def handle_data(self, data):
        data = data.strip()
        if data:
            if self.in_title:
                print(data)
            elif self.in_header:
                print(data)

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False
        elif tag.startswith('h') and tag[1:].isdigit():
            self.in_header = False

def extract_headers_and_title(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        content = file.read()

    parser = HTMLParser()
    parser.feed(unescape(content))

if len(sys.argv) != 2:
    print("Пожалуйста, укажите путь к HTML-файлу как аргумент командной строки.")
else:
    html_file_path = sys.argv[1]
    extract_headers_and_title(html_file_path)