#
# * 1
# from PIL import Image
# from PIL import UnidentifiedImageError
# from io import BytesIO
# import requests

# url = input()
# r = requests.get(url)

# try:
#     r.raise_for_status()
#     i = Image.open(BytesIO(r.content))
#     i.save("secret_file.jpg")
#     print("File saved")

# except requests.exceptions.HTTPError as e:
#     # Обработка 404, 500 и других HTTP-ошибок
#     print(
#         f"[ПРОВАЛ: СЕТЬ] Сервер вернул ошибку {r.status_code}. Ссылка не ведет на файл или недоступна."
#     )
#     print(f"Детали: {e}")

# except UnidentifiedImageError:
#     # Обработка случая, когда загруженные данные - не изображение
#     print(
#         f"[ПРОВАЛ: КОНТЕНТ] Данные загружены, но не являются распознаваемым изображением (вероятно, HTML-страница или поврежденный файл)."
#     )

# except requests.exceptions.RequestException as e:
#     # Обработка других сетевых ошибок (например, ConnectionError, Timeout)
#     print(f"[ПРОВАЛ: СЕТЬ] Произошла ошибка соединения или таймаут: {e}")

# except Exception as e:
#     # Общий обработчик для непредвиденных ошибок
#     print(f"[ПРОВАЛ: НЕПРЕДВИДЕННАЯ] Произошла ошибка: {e}")


# * 2
# Вы — главный оператор специального центра мониторинга веб-сайтов. Ваша
# задача — выполнять регулярную проверку доступности важных веб-порталов по
# всему миру. Ваш центр ответственен за обеспечение непрерывной работы этих
# веб-сайтов, поэтому вам необходимо иметь набор инструментов для
# мониторинга и проверки статуса.
# Ваша программа выполняет проверку доступности веб-сайтов, введенных вами
# в список `urls`. Она производит HTTP-запросы к каждому сайту и проверяет
# статус код ответа. Если статус код равен 200, сайт считается доступным, и
# вы выводите сообщение об этом. В противном случае, вы указываете в
# сообщении, что сайт недоступен, и выводите соответствующий статус код
#

# * 3
# Вы — главный разработчик приложения для цитат из аниме. Вы решаете
# использовать [API](https://docs.waifu.it/rest-api/texts/quote/search),
# чтобы предоставить пользователям широкий спектр цитат из разных аниме для
# их вдохновения.
# Напишите программу, которая превратит ваш компьютер в сокровищницу аниме-
# цитат! Каждый раз, когда вы запускаете программу, она будет выводить на
# экран случайную и вдохновляющую цитату из самых известных аниме
# import requests
# import json

# TOKEN = "NTM2MTkwNTYzMDM3MjE2ODEw.MTc1OTgzMzUyOA--.e3ea59efda03"


# url = "https://waifu.it/api/v4/quote"
# response = requests.get(
#     url,
#     headers={
#         "Authorization": TOKEN,
#     },
# )
# data = response.json()

# print(data["quote"])

# input_string = data["quote"]

# import random
# from colorama import Fore, Style, init

# # Инициализация Colorama для корректной работы на разных ОС (особенно Windows)
# init(autoreset=True)


# def colorize_randomly(text):
#     """
#     Раскрашивает каждое слово в строке в случайный цвет, используя Colorama.
#     """
#     # 1. Список доступных цветов Fore (текст)
#     # Исключаем BLACK и RESET, которые могут быть неразличимы или сбросят стиль
#     available_colors = [
#         Fore.RED,
#         Fore.GREEN,
#         Fore.YELLOW,
#         Fore.BLUE,
#         Fore.MAGENTA,
#         Fore.CYAN,
#         Fore.WHITE,
#     ]

#     # 2. Разбиваем строку на слова
#     words = text.split()
#     colored_parts = []

#     # 3. Перебираем слова и назначаем случайный цвет
#     for word in words:
#         # Выбираем случайный цвет из списка
#         random_color = random.choice(available_colors)

#         # Объединяем код цвета, слово и сброс стиля (Style.RESET_ALL)
#         # init(autoreset=True) делает сброс автоматическим, но явное
#         # использование гарантирует, что только это слово будет окрашено.
#         colored_word = f"{random_color}{word}{Style.RESET_ALL}"
#         colored_parts.append(colored_word)

#     # 4. Соединяем слова обратно в строку с пробелами
#     return " ".join(colored_parts)


# colored_output = colorize_randomly(input_string)

# print(colored_output)

# * 4
# Вы отправляетесь в увлекательное путешествие по всему миру в роли
# знаменитого путешественника. Ваша задача — узнать актуальную погоду в
# любом городе, чтобы быть на шаг впереди и адаптироваться к любым
# природным условиям. Ведь только настоящие путешественники знают, что
# знание погоды — ключ к успеху!
# Чтобы получить данные о погоде в заданном городе, вам нужно всего лишь
# написать программу, которая будет принимать на вход название города и
# связываться с [волшебным API погодного
# сервиса](https://www.weatherapi.com/), чтобы достать самые точные и
# надежные данные о погоде в указанном городе
# import requests
# import json

# API_KEY = "5549310096544d9292f141631250610"
# city = input("Введите город: \n")
# DAYS_COUNT = 3
# API_URL = "https://api.weatherapi.com/v1/forecast.json"

# params = {
#     "key": API_KEY,
#     "q": city,
#     "days": DAYS_COUNT,
#     "aqi": "no",  # Без данных о качестве воздуха
#     "alerts": "no",  # Без погодных предупреждений
#     "lang": "ru",  # На русском языке
# }

# try:
#     response = requests.get(API_URL, params=params)
#     response.raise_for_status()

#     data = response.json()

#     current_temp = data["current"]["temp_c"]
#     current_condition = data["current"]["condition"]["text"]

#     tomorrow_forecast = data["forecast"]["forecastday"][1]["day"]
#     max_temp_tomorrow = tomorrow_forecast["maxtemp_c"]
#     min_temp_tomorrow = tomorrow_forecast["mintemp_c"]

#     print(f"Город: {data['location']['name']}")
#     print(f"Текущая температура: {current_temp}°C ({current_condition})")
#     print(f"Прогноз на завтра:")
#     print(f" Максимум: {max_temp_tomorrow}°C")
#     print(f" Минимум: {min_temp_tomorrow}°C")

# except requests.exceptions.RequestException as e:
#     print(f"Ошибка запроса: Проверьте ключ, соединение и URL. Детали: {e}")
# except KeyError:
#     print(
#         "Ошибка: Некорректный формат ответа JSON. Проверьте, что ключ верен и город найден."
#     )

# * 5

# Вы — молодой и предприимчивый программист, который мечтает работать на
# валютной удаленке в хорошей компании. Чтобы всегда получать актуальный и
# точный прогноз курса валют, вы решили написать программу, которая будет
# запрашивать у пользователя сумму в одной валюте и конвертировать ее в
# другую валюту. Программа должна выполнить конвертацию с помощью сетевого
# запроса к [API конвертера валют](https://freecurrencyapi.com/)
# import requests
# import pprint

# # выводит сколько 18 долларов будет в введеной валюте
# API_KEY = "fca_live_oOcpldfAB02dOJBhZtKufu78rCnzMx4z6HmOfwyG"
# try:
#     user_summ = float(input("Введите сумму, которую хотите конвертировать\n"))
# except ValueError:
#     print("Введите сумму цифрами")
# user_currency = input(
#     "Введите трёхбуквенный алфавитный код валюты в формате ISO 4217\n"
# ).upper()
# r = requests.get(f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}")
# data = r.json()

# try:
#     currency = data["data"][user_currency]
# except KeyError:
#     print("Введите верный код валюты")
# else:
#     print(f"{currency*user_summ:.2f}")


# * 6
# В процессе длительного путешествия по всему миру вы обнаружили, что
# неудобно каждый раз запускать программу чтобы посмотреть погоду. Поэтому
# вы решили улучшить свою программу таким образом, чтобы она отображала
# график, построенный с помощью matplotlib, отображающий прогноз погоды в
# течение N дней (например, на неделю вперёд)
# import requests
# import matplotlib.pyplot as plt

# API_URL = "https://api.weatherapi.com/v1/forecast.json"
# API_KEY = "5549310096544d9292f141631250610"
# # * CITY = input("Введите город: \n")
# CITY = "Moscow"
# try:
#     days_count = int(input("Введите количество дней, не более 14\n"))
# except ValueError:
#     print("Введено НЕ число")


# params = {"key": API_KEY, "q": CITY, "days": days_count, "lang": "ru", "alerts": "yes"}

# try:
#     response = requests.get(API_URL, params=params)
#     response.raise_for_status()
#     data = response.json()

# except requests.exceptions.RequestException as e:
#     print(f"Ошибка запроса: Проверьте ключ, соединение и URL. Детали: {e}")
# except KeyError:
#     print(
#         "Ошибка: Некорректный формат ответа JSON. Проверьте, что ключ верен и город найден."
#     )
# max_t = [
#     data["forecast"]["forecastday"][x]["day"]["maxtemp_c"] for x in range(days_count)
# ]
# min_t = [
#     data["forecast"]["forecastday"][x]["day"]["mintemp_c"] for x in range(days_count)
# ]


# plt.figure()
# plt.title("Погода на х дней: макс и мин")
# plt.ylabel("t 'C")
# plt.xlabel("День")
# plt.plot(range(1, days_count + 1), max_t, "r-")
# plt.plot(range(1, days_count + 1), min_t, "b--")
# plt.yticks(ticks=range(20))
# plt.grid()
# plt.show()


# * Задача 7
# Вы — молодой ученый, который работает в космическом исследовательском
# центре и мечтает о том, чтобы увидеть Землю из космоса. Однажды вы
# слышите о планируемой миссии космического аппарата, который должен
# отправиться на орбиту и сделать уникальные снимки Земли.
# Вы горите желанием узнать больше о миссии и о том, какие фотографии будут
# сделаны. Вы начинаете изучать все подробности и обнаруживаете, что именно
# 7 июля 2022 года будут сняты фотографии Земли. Используя свои программные
# навыки и [NASA API](https://api.nasa.gov/), создайте специальную
# программу для скачивания этих изображений и сохранения их в формате GIF.
# ! shutdown ALRAM !


# import requests
# import io
# from PIL import Image

# # 1. КОНСТАНТЫ МИССИИ
# # Базовый URL для получения списка снимков за дату
# API_LIST_URL = "https://api.nasa.gov/EPIC/api/natural/date/2022-07-07"
# # Базовый URL для скачивания самого изображения (JPEG)
# IMAGE_BASE_URL = "https://api.nasa.gov/EPIC/archive/natural/2022/07/07/jpg/"
# # Ваш API-ключ от NASA. Используйте 'DEMO_KEY' для тестирования.
# NASA_API_KEY = "DEMO_KEY"
# OUTPUT_FILENAME = "Earth_EPIC_20220707.gif"


# def download_and_create_gif():
#     """Загружает все изображения EPIC за 7 июля 2022 года и объединяет их в GIF."""

#     print("--- Начало операции EPIC-Download ---")

#     # Параметры запроса (API-ключ)
#     params = {"api_key": NASA_API_KEY}

#     # 1. Получение списка доступных снимков
#     try:
#         response = requests.get(API_LIST_URL, params=params)
#         response.raise_for_status()
#         image_data_list = response.json()
#     except requests.exceptions.RequestException as e:
#         print(f"❌ Ошибка при получении списка файлов: {e}")
#         return

#     if not image_data_list:
#         print("⚠️ Не удалось найти снимки за 2022-07-07. Проверьте дату или API-ключ.")
#         return

#     print(f"✅ Найдено {len(image_data_list)} снимков. Начинаем загрузку...")

#     downloaded_images = []

#     # 2. Итерация и загрузка каждого снимка
#     for item in image_data_list:
#         # Имя файла извлекается из данных JSON
#         file_name = item["image"] + ".jpg"

#         # Полный URL для загрузки конкретного файла
#         image_url = f"{IMAGE_BASE_URL}{file_name}"

#         try:
#             # Загрузка бинарных данных изображения
#             img_response = requests.get(image_url, params=params)
#             img_response.raise_for_status()

#             # Чтение данных в объект BytesIO в памяти
#             image_stream = io.BytesIO(img_response.content)

#             # Открытие изображения с помощью Pillow
#             img = Image.open(image_stream)
#             downloaded_images.append(img)
#             print(f"   Загружено: {file_name}")

#         except (requests.exceptions.RequestException, IOError) as e:
#             print(f"   ❌ Ошибка при загрузке {file_name}: {e}")
#             continue

#     if not downloaded_images:
#         print("❌ Не удалось загрузить ни одного изображения.")
#         return

#     # 3. Создание GIF-анимации
#     print("🔄 Объединение снимков в GIF-анимацию...")

#     # Берем первое изображение как основу
#     first_image = downloaded_images[0]

#     # Сохраняем в формате GIF. duration=200 - задержка в миллисекундах между кадрами.
#     first_image.save(
#         OUTPUT_FILENAME,
#         save_all=True,
#         append_images=downloaded_images[1:],
#         duration=200,
#         loop=0,  # 0 означает бесконечный цикл
#     )

#     print(f"🎉 Миссия выполнена! Файл GIF сохранен как: {OUTPUT_FILENAME}")
#     print("Теперь вы можете увидеть Землю в движении, молодой ученый!")


# if __name__ == "__main__":
#     download_and_create_gif()


# * 8
import requests
import folium

IP = "115.41.218.39"
r = requests.get(f"http://ip-api.com/json/{IP}")
data = r.json()
m = folium.Map(location=(data["lat"], data["lon"]))
m.save("index.html")
