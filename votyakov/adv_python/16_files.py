# * 1
def all_file(file):
    with open(file, encoding="utf-8") as f:
        return f.read()


# print(all_file("input.txt"))


# * 2
def one_line(file):
    with open(file, encoding="utf-8") as f:
        return f.readline()


# print(one_line("input.txt"))


# * 3
def all_lines(file):
    with open(file, encoding="utf-8") as f:
        L1 = f.readlines()
        return L1


# print(all_lines("input.txt"))


# * 4
def all_lines_stripped(file):
    with open(file, encoding="utf-8") as f:
        s = f.read()
        l1 = s.split("\n")
        return l1


# print(all_lines_stripped("input.txt"))


# * 5
def all_lines_printer(file):
    with open(file, encoding="utf-8") as f:
        for line in f:
            print(line)


# all_lines_printer("input.txt")


# * 6
def spaced_lines(file):
    with open(file, encoding="utf-8") as f:
        f = f.read()
        s = f.split()
        s = " ".join(s)
        return s


# print(spaced_lines("input.txt"))

s1 = "Далее копируем весь текст который появляется при нажатии на файл."


# * 7
def stripped_line(string):
    return string.rstrip(" \n\t")


print(stripped_line(s1))


s = "Далее копируем весь текст который появляется при нажатии на файл."


# * 8
def no_punctuation(string):
    return string.rstrip("!?.")


print(no_punctuation(s))
