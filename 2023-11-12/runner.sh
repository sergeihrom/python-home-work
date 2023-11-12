#!/bin/bash

# Пеереход в каталог
cd ../2023-11-09


# Вывод всех файлов в каталоге 2023-11-09

echo "Список файлов  в   каталоге 2023-11-09"
ls 

# запуск  ppyhon  скриптов с предыдущего дз

echo "запуск week1.py"
python3 week1.py
echo "запуск week2.py"
python3 week2.py
cd ../2023-11-12

# Копирование файла 
cp runner.sh runner_copy.sh

echo "Cписок файлов в каталоге 2023-11-12"
ls
