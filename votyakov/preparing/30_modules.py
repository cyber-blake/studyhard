#
# * 1
import statistics
from statistics import *
from statistics import mean
from statistics import mean as m
import statistics as s

x = [4, 2]
print(mean(x))

# * 2
help("modules")
# ?
import sys

for x in sys.modules:
    print(x)

print(dir())


# ? show_console_commands()
# * 3
import sys

sys.setrecursionlimit(2000)


def recursive_function(n, sum):
    if n < 1:
        return sum
    else:
        return recursive_function(n - 1, sum + n)


print(recursive_function(1000, 0))

# ответ: 500500
# * 4
text = "ул. Кутузовская, дом №13, корпус 3, квартира 98"
from re import findall

res = findall("\d+", text)
print(res)

# * 5
from random import randint as rnd
from random import choice as chc

array = [rnd(1, 100) for x in range(10)]
print(array)
print(chc(array))

# * 6
# a, b, c = list(map(float, input().split()))

# import math


# print(f"Уравнение: {a}x^2 + {b}x + {c} = 0")

# if a == 0:
#     if b == 0:
#         print("Бесконечно много решений" if c == 0 else "Нет решений")
#     else:
#         print(f"Ответ: x = {-c/b}")
# else:
#     D = b * b - 4 * a * c

#     if D > 0:
#         x1 = (-b - math.sqrt(D)) / (2 * a)
#         x2 = (-b + math.sqrt(D)) / (2 * a)
#         print(f"Два корня: x1 = {x1}, x2 = {x2}")
#     elif D == 0:
#         x = -b / (2 * a)
#         print(f"Один корень: x = {x}")
#     else:
#         print("Действительных корней нет")
# * 7
import datetime

print(datetime.datetime.now().time())

# * 8
# ответ: 8 Вторник

# * 9
import py_version

py_version.get_ver()

# * 10
from calculator import *

print(add(7, 4))
print(subtract(1, 4))
print(multiply(7, 4))
print(divide(7, 4))
print(divide("7", 4))
print(divide(7, 0))
# * 11
import imp_modules

imp_modules.imp_modules(["math", "random"])

print(math.factorial(random.randint(0, 10)))
# * 12
import geometry

print(geometry.triangle(78, 55, 80))
print(geometry.triangle())

print(geometry.square())
