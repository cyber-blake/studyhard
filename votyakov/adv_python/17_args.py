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
    return


# **kwargs - список строк переменной длины
# *args - передача значения мин_ленгтх
# * возвращает список строк

strings = ["hello", "world", "how", "are", "you"]
print(filter_by_length(4, *strings))
print(filter_by_length(3, *strings))
