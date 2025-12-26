def ignore_command(command):
    ignore = [
        "alias",
        "configuration",
        "ip",
        "sql",
        "select",
        "update",
        "exec",
        "del",
        "truncate",
    ]
    return not all(item not in command for item in ignore)


# * Встроенная функция all() возвращает значение True, если все элементы переданной ей последовательности (итерируемого объекта) истинны (приводятся к значению True), или False в противном случае.

# ? Перепишите функцию ignore_command(), чтобы она использовала встроенные функции all()/any(), сохранив при этом ее функционал.


print(ignore_command("get ip"))
print(ignore_command("select all"))
print(ignore_command("delete"))
print(ignore_command("trancate"))
