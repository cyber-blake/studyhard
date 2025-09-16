#
# * 1
def timer(func):
    import time

    def inside(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter() - start
        print(f"Функция {func.__name__} поработала {end:.4f} сек")
        return result

    return inside


# * 2
def casher(func):
    D = dict()

    def inside_func(x):
        if x not in D:
            D[x] = func(x)
        return D[x]

    return inside_func


# * 3
def logging(func):

    def inside(*args, **kwargs):
        with open("output.txt", "a") as f:
            print(*args, **kwargs, file=f)
        print(f"Логи функции {func.__name__} были записаны в файл output.txt")

    return inside


# * 4
def retry(tries=3):
    import time

    def decorator(func):
        def wrapper(*args, **kwargs):
            returning = tries
            while returning > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Попытка не удалась: {e}. Осталось {returning - 1} попыток.")
                    returning -= 1
                    time.sleep(1)  # Ждем перед следующей попыткой

            raise Exception("Удаленный хост недоступен.")

        return wrapper

    return decorator


# ? trying my decorators
@retry(5)
@logging
def get_data():
    import random

    if random.random() > 0.4:
        raise IOError("Сетевая ошибка!")
    return "Данные успешно получены."


try:
    print(get_data())
except Exception as e:
    print(f"Ошибка: {e}")


def fib(x):
    if x <= 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


@timer
def calc_fib(n):
    for n in range(n):
        result = fib(n)
        print(f"fib({n}) = {result}")


calc_fib(36)


@timer
def waiting():
    import time

    time.sleep(2)
    print("Completed!")


waiting()
