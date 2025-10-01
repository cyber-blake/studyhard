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
import psutil

for x in dir(psutil):
    print(x)

print(psutil.__dict__)
# print(psutil.cpu_times())
for x in range(4):
    print(psutil.cpu_percent(interval=1))

print(psutil.net_io_counters(pernic=True))
print(psutil.sensors_battery())
