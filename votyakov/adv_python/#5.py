def custom_print(*args, **kwargs):

    try:
        if sep:  # если обьявлена в кваргс
            pass
    except NameError:  # если sep не обьявлена
        sep = " "

    try:
        if end:  # если обьявлена в кваргс
            pass
    except NameError:  # если end не обьявлена
        end = "\n"
    l = []
    # * сначала приводим к одному виду список, key,values склеиваем в строку
    if args:
        l.extend(args)
    if kwargs:
        for key, value in kwargs.items():
            l.append(f"{key}={value}")
    new_list = l[:]
    # * список без сеп и енд
    for x in new_list:
        if isinstance(x, str) and x.startswith("sep"):
            new_list.remove(x)

        if isinstance(x, str) and x.startswith("end"):
            new_list.remove(x)
    # ? проверить если в словаре есть ключи сеп или енд
    # ? если есть - то в перем сеп записать ключ "сеп", и в перем енд записать
    # ? кваргс.кей = сеп,
    print("общий список всех аргсов")
    print(*l, sep=sep, end=end)
    print("список аргсов без сеп и енд")
    print(new_list)
    print()


custom_print(1, 2, 3, a=4, b=5, sep="-", end="!")
# 1-2-3-a=4-b=5!
custom_print("Hello", "World", sep=" ")
# Hello World
custom_print("apple", "banana", "cherry", sep=", ")
# apple, banana, cherry
custom_print(a=1, b=2, end="...")
# a=1 b=2...
# вот это я наворотил... зато Использовал то, что знаю!
