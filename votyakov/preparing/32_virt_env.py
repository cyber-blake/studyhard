#
# * 3
# Requires: EasyProcess, entrypoint2, mss
# Required-by:

import pyscreenshot as ImageGrab

# import time

# im = ImageGrab.grab()

# sv = im.save("fullscreen2.png")

# print(im.__dict__)
# print(im.save.__dict__)


# array = []

# for _ in range(5):
#     array.append(ImageGrab.grab())
#     time.sleep(1)

# for x, y in enumerate(array):
#     y.save(f"shot №{x}.png")


# * 4
import thefuzz
from thefuzz import fuzz
from thefuzz import process

for x in dir(thefuzz):
    print(x)

print(thefuzz.fuzz.__dict__)

s1 = "Я разобрался с виртуальным окружением"
s2 = "Это оказалось совсем не трудно"
s3 = "Я разобрался с виртуальным окружением!"
s4 = "Я разобрался с виртуальным окружением!"
s5 = "Я разобрался с виртуальным окружением?"
s6 = "Я разобрался с виртуальным окружением!"

print(fuzz.ratio(s1, s2), "%")
print(fuzz.ratio(s3, s4), "%")
print(fuzz.ratio(s5, s6), "%")


# * 5
# import psutil

# for x in dir(psutil):
#     print(x)

# print(psutil.__dict__)
# # print(psutil.cpu_times())
# for x in range(4):
#     print(psutil.cpu_percent(interval=1))

# print(psutil.net_io_counters(pernic=True))
# print(psutil.sensors_battery())

# * 6
import pyttsx3
import psutil

engine = pyttsx3.init()
battery_info = psutil.sensors_battery()
print(engine.say.__dict__)
if battery_info:
    if battery_info.power_plugged:
        if battery_info.percent < 20:
            engine.say("АЛЯРМ! БАТАРЕЯ ПОЧТИ РАЗРЯЖЕНА!")
            engine.runAndWait()
else:
    print("ALARM! BATTERY NOT FOUND!")


# * 7

# import win11toast

# print("Модули пакета win11toast:")
# print([x for x in dir(win11toast)])


# win11toast.toast("Hello World!")


# import time
# import datetime
# from win11toast import toast


# def validate_time(alarm_time):
#     """Проверка времени в формате HH:MM"""
#     try:
#         hours, minutes = map(int, alarm_time.split(":"))
#         return 0 <= hours <= 23 and 0 <= minutes <= 59
#     except:
#         return False


# def main():
#     print("ПРОСТОЙ БУДИЛЬНИК")

#     # Ввод времени
#     alarm_time = input("Введите время (HH:MM): ")

#     if not validate_time(alarm_time):
#         print("Неверное время!")
#         return

#     # Ввод названия
#     alarm_name = input("Название будильника: ") or "Будильник"

#     print(f"Будильник '{alarm_name}' на {alarm_time} установлен!")

#     # Ожидание
#     while True:
#         now = datetime.datetime.now().strftime("%H:%M")
#         if now == alarm_time:
#             # Уведомление
#             toast(
#                 "Будильник!",
#                 f"Время для: {alarm_name}",
#                 button="Выключить",
#                 duration="long",
#             )
#             print(" Будильник сработал")
#             break
#         time.sleep(30)


# if __name__ == "__main__":
#     main()


# * 8
import dotenv
from dotenv import load_dotenv
import os

for attr in dir(dotenv):
    if not attr.startswith("_"):  # Показываем только публичные
        print(f"{attr}")


# main.py


def main():
    load_dotenv()

    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    api_key = os.getenv("API_KEY")
    database_url = os.getenv("DATABASE_URL")
    secret_key = os.getenv("SECRET_KEY")

    print("Значения приватных переменных:")
    print(f"USERNAME: {username}")
    print(f"PASSWORD: {password}")
    print(f"API_KEY: {api_key}")
    print(f"DATABASE_URL: {database_url}")
    print(f"SECRET_KEY: {secret_key}")

    # Проверяем, что все переменные загружены
    if all([username, password, api_key, database_url, secret_key]):
        print("\nВсе переменные успешно загружены!")
    else:
        print("\nВнимание: некоторые переменные не были загружены!")


if __name__ == "__main__":
    main()
