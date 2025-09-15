#
# * 1
from functools import cache


def logging(func):

    def inside(*args, **kwargs):
        with open("output.txt", "w") as f:
            print(*args, **kwargs, file=f)
        print(f"Логи функции {func.__name__} были записаны в файл output.txt")
        return

    return inside


def timer(func):
    import time

    def inside(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter() - start
        print(f"Функция {func.__name__} поработала {end:.4f} сек")
        return result

    return inside


@logging
@timer
def fib(x):
    if x <= 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


for n in range(19):
    result = fib(n)
    print(f"fib({n}) = {result}")


@timer
@logging
def quarter(x):
    s = 0
    for i in range(x):
        s += x**4
    return s


print(quarter(1000))


# * 3
def logging(func):

    def inside(*args, **kwargs):
        with open("output.txt", "a") as f:
            print(*args, **kwargs, file=f)
        print(f"Логи функции {func.__name__} были записаны в файл output.txt")
        return

    return inside
