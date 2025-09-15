#
# * 1
def sum_numbers(*args):
    return sum(args)


print(sum_numbers(1, 2, 3))


# * 2
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Alice", age=25, country="USA")

# * 3


def filter_by_length(min_length, *strings):
    """
    Создайте функцию filter_by_length, которая будет принимать список строк
    и дополнительный аргумент min_length. Функция должна использовать kwargs
    для передачи списка строк переменной длины и args для передачи значения
    min_length. Функция должна вернуть новый список, содержащий только те строки, длина которых больше или равна min_length
    """
    a = []
    for x in strings:
        if len(x) >= min_length:
            a.append(x)
    return a


# **kwargs - список строк переменной длины
# *args - передача значения мин_ленгтх
# * возвращает список строк

strings = [
    "hello",
    "world",
    "how",
    "are",
    "you",
]
print(filter_by_length(4, *strings))
print(filter_by_length(3, *strings))


# * 4
def calculate_total_price(price, **kwargs):
    """
    Реализуйте функцию calculate_total_price, которая принимает на вход стоимость товара и произвольное количество ключевых аргументов, где каждый ключ представляет собой тип скидки, а значение — размер скидки в процентах. Функция должна вернуть общую стоимость товара после применения скидок
    """
    vals = 0
    for k, v in kwargs.items():
        vals += v
    return price * (100 - vals) / 100


print(calculate_total_price(100, student=10, coupon=20))  # 70.0
print(calculate_total_price(200, holiday=25))  # 150.0
print(calculate_total_price(500))


# * 5


def custom_print(*args, **kwargs):

    l = []
    sep = kwargs.pop("sep", " ")  # Удаляем из kwargs и получаем значение
    end = kwargs.pop("end", "\n")
    # * сначала приводим к одному виду список, key,values склеиваем в строку
    if args:
        l.extend(args)
    if kwargs:
        for key, value in kwargs.items():
            l.append(f"{key}={value}")
    print(*l, sep=sep, end=end)


custom_print()
custom_print(1, 2, 3, a=4, b=5, sep="-", end="!")
# 1-2-3-a=4-b=5!
custom_print()
custom_print("Hello", "World", sep=" ")
# Hello World
custom_print("apple", "banana", "cherry", sep=", ")
# apple, banana, cherry
custom_print(a=1, b=2, end="...")
# a=1 b=2...
