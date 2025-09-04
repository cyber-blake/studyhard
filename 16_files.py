def all_file(file):
    with open(file, encoding="utf-8") as f:
        return f.read()


# print(all_file("input.txt"))


def one_line(file):
    with open(file, encoding="utf-8") as f:
        return f.readline()


# print(one_line("input.txt"))


def all_lines(file):
    with open(file, encoding="utf-8") as f:
        L1 = f.readlines
        return L1


# print(all_lines("input.txt"))
