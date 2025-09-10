def mean(*args):
    s = 0
    l = []
    for x in args:
        if type(x) in (int, float):
            l.append(x)
    s += sum(l)
    try:
        return s / len(l)
    except ZeroDivisionError:
        return 0.0


print(mean())
print(mean(7))
print(mean(1.5, True, ["stepik"], "beegeek", 2.5, (1, 2)))
print(mean(True, ["stepik"], "beegeek", (1, 2)))
print(mean(-1, 2, 3, 10, ("5")))
print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
