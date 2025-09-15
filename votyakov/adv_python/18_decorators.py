#
# * 1
from functools import cache


def timer(func):
    import time

    def inside(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter() - start
        print(f"Функция {func.__name__} поработала {end:.4f} сек")
        return result

    return inside


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
def quarter(x):
    s = 0
    for i in range(x):
        s += x**4
    return s


print(quarter(1000))
