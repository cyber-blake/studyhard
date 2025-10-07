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
import requests

API_KEY = "fca_live_oOcpldfAB02dOJBhZtKufu78rCnzMx4z6HmOfwyG"
site = input("Введите сумму")
r = requests.get(https://api.freecurrencyapi.com/v1/latest?apikey=API_KEY)
