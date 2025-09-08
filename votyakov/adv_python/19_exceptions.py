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
def filter_hex_string(string):
    try:
        int(string, 16)
        return True
    except ValueError:
        return False


# задача: чтобы в список попадали те строки, которые проходят фильтр
# для этого нужно подать список строк, -> разбив одну строку через пробел
def check_password(*args):
    args = list(args)
    args = args.split()
    return filter(filter_hex_string, args)


print(list(check_password(input())))
