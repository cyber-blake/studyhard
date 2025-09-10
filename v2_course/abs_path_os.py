import os

# Получить директорию где находится скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "prices.txt")

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()
