#
# * 0
# pip install howdoi

# * 1
import requests


def status_report(site):
    r = requests.get(site)
    code = r.status_code
    if code == 200:
        return "Alles normales"
    else:
        return "Critical error"


print(status_report("https://votyakov.getcourse.ru"))
print(status_report("https://requests.readthedocs.io"))


# * 2
def resize(file):
    from PIL import Image

    try:
        img = Image.open(file)
        print("Размер изображения:")
        print(img.format, img.size, img.mode)
        size = (128, 128)
        saved = "lenna.jpeg"
        img.thumbnail(size)
        img.save("resized_test.jpg")
    except FileNotFoundError:
        print("Файл не найден")


resize("C:\\Users\\Пользователь\\Downloads\\Lenna.png")

# * 3
from pytube import YouTube

# video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# yt = YouTube(video_url)
# stream = yt.streams.get_highest_resolution()
# stream.download()
# print("Download complete!")

# * 4
from colorama import Fore, Back, init, Style

init()

print(Back.WHITE + "Russia is our sacred state")
print(Back.BLUE + "Russia is our beloved country.")
print(Back.RED + "A mighty will, great glory -")
print(Style.RESET_ALL + "Your dignity for all time!")
print(Fore.LIGHTBLACK_EX + "...music playing..." + Style.RESET_ALL)


# * 5
import emoji

print(emoji.demojize("Buy the programming after 👀 school👏📚🏫 course!😂"))


# * 6
import pyperclip
import time


def clean_and_normalize(text):
    """
    Применяет все правила преобразования к заданной строке.

    Правила:
    1. Все буквы 'ё' заменяются на 'е'.
    2. Все буквы становятся строчными.
    3. Лишние пробелы и табуляции удаляются.
    """
    # 1. Замена 'ё' на 'е' (так как будет преобразовано в нижний регистр)
    text = text.replace("ё", "е").replace("Ё", "Е")

    # 2. Все заглавные буквы заменяются на строчные
    text = text.lower()

    # 3. Удаление лишних пробелов:
    #    - .split() разбивает строку по любому количеству пробелов/табов/переносов и отбрасывает пустые строки
    #    - " ".join() соединяет оставшиеся слова одним пробелом
    text = " ".join(text.split())

    return text


def clipboard_cleaner_loop():
    last_processed_content = ""

    while True:
        try:
            current_content = pyperclip.paste()

            if current_content != last_processed_content:
                processed_content = clean_and_normalize(current_content)

                if current_content != processed_content:
                    pyperclip.copy(processed_content)
                    print(
                        f"\n[ОЧИЩЕНО] Старое: '{current_content.strip()[:30]}...' -> Новое: '{processed_content}'"
                    )

                last_processed_content = processed_content

            time.sleep(1)

        except KeyboardInterrupt:
            # Обработка остановки пользователем
            print("\n--- Программа остановлена пользователем ---")
            break
        except pyperclip.PyperclipException as e:
            # Обработка возможных ошибок, связанных с доступом к буферу обмена
            print(
                f"\n[ОШИБКА] Не удалось получить доступ к буферу обмена: {e}. Повтор через 1 сек."
            )
            time.sleep(1)
        except Exception as e:
            print(f"\n[КРИТИЧЕСКАЯ ОШИБКА] {e}")
            time.sleep(1)


if __name__ == "__main__":
    clipboard_cleaner_loop()


# * 7
import wikipedia

# Получение информации о странице
page = wikipedia.page("Python programming language")
print(page.content)

# Получение случайной страницы
random_page = wikipedia.random()
print(random_page)

# Пожертвование на поддержку проекта
wikipedia.donate()
