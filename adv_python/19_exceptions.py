# * 1
def calc(str):
    a, b, op = str.split()
    a = float(a)
    b = float(b)
    try:
        return a / b
    except ZeroDivisionError:
        return "ERROR"


# print(calc(input()))


# * 2
def check(*args):
    try:
        x = filter(lambda x: int(x, 16), args)
        return x
    except ValueError:
        return "this cannot"
    except TypeError:
        pass


# print(list(check("abc", "asd", "opj")))
# x = ("abc", "asd", "opj")
# for each in x:
#     if int(x, 16):
#         print(x)

numbers = range(11)


# функция, которая проверяет числа
def filter_odd_num(in_num):
    if (in_num % 2) == 0:
        return True
    else:
        return False


# Применение filter() для удаления нечетных чисел
out_filter = filter(filter_odd_num, numbers)

print("Тип объекта out_filter: ", type(out_filter))
print("Отфильтрованный список: ", list(out_filter))
