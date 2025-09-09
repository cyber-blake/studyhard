#
# * 1
def all_file(file):
    with open(file, encoding="utf-8") as f:
        return f.read()


print(all_file("input.txt"))


# * 2
def one_line(file):
    with open(file, encoding="utf-8") as f:
        return f.readline()


print(one_line("input.txt"))


# * 3
def all_lines(file):
    with open(file, encoding="utf-8") as f:
        L1 = f.readlines()
        return L1


print(all_lines("input.txt"))


# * 4
def all_lines_stripped(file):
    with open(file, encoding="utf-8") as f:
        s = f.read()
        l1 = s.split("\n")
        return l1


print(all_lines_stripped("input.txt"))


# * 5
def all_lines_printer(file):
    with open(file, encoding="utf-8") as f:
        for line in f:
            print(line)


all_lines_printer("input.txt")


# * 6
def spaced_lines(file):
    with open(file, encoding="utf-8") as f:
        f = f.read()
        s = f.split()
        s = " ".join(s)
        return s


print(spaced_lines("input.txt"))

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


# * 9
def write_string(file, string):
    with open(file, "a", encoding="utf-8") as f:
        f = f.write(string)


write_string("input.txt", "Hallo Welt!")


# * 10
def write_string_v2(file, string):
    with open(file, "a", encoding="utf-8") as f:
        string += "\n"
        f = f.write(string)


write_string_v2("input.txt", "Hola mundo!")


# * 11
def write_lines(file, list1):
    with open(file, "a", encoding="utf-8") as f:
        f = f.writelines(list1)


l = ["abc", "def", "ghi", "jkl", "mno", "pqrs"]
write_lines("input.txt", l)


# * 12
def transport(file1, file2):
    with open(file1, encoding="utf-8") as f1:
        content = f1.read()
    with open(file2, "w", encoding="utf-8") as f2:
        print(content, file=f2)


transport("input.txt", "output.txt")


# * 13
def lines_in_between(A, B):
    """
    13. функция, которая принимает на вход сначала имя первого файла, затем имя
    второго файла, а после записывает во второй файл все строки, которые на-
    чинаются с подстроки <hello>, а заканчиваются на подстроку <world>. Ис-
    пользуйте методы .startswith() и .endswith()
    """
    with open(A, "r", encoding="utf-8") as f:
        with open(B, "w", encoding="utf-8") as g:
            for line in f:
                tempLine = line.strip()
                if tempLine.startswith("hello") and tempLine.endswith("world"):
                    g.write(line)


# * 14
def processDictionary(name):
    dictionary = []
    with open(name, "r", encoding="utf-8") as f:
        data = f.readlines()[1:]
    for line in data:
        temp = line.split()
        dictionary[temp[0]] = (temp[1], temp[2])
    return dictionary
