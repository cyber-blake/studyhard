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


# print(list(check_password(input())))


# * 3
olympiad1 = {
    "name": "Пробная вышка",
    "winners": {
        "Олеся Олимпиадникova": 594,
        "Олег Олимпиадников": 587,
        "Онисим Олимпиадников": 581,
    },
}

olympiad2 = {
    "name": "Горные воробьи",
    "winners": {
        "Ольга Олимпиадникова": (20, 20, 19, 20),
        "Олеся Олимпиадникова": (19, 19, 20, 20, 17),
        "Офелия Олимпиадникова": (20, 20, 20, 20, 13),
    },
}

for x, y in olympiad1.items():
    print(x, y)

# Проход по всем уровням
for key, value in olympiad1.items():
    if isinstance(value, dict):
        print(f"{key}:")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {sub_value}")
    else:
        print(f"{key}: {value}")
