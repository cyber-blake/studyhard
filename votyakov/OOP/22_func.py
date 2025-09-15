#
# * 1
def factorial(n):
    return n * factorial(n - 1) if n else 1


# * 2
def is_prime(n):
    return False if [x for x in range(2, n) if n % x == 0] else True


# * 3
numbers = [8, 14, 65, 43, 76, 11, 13, 15, 126]


def filter_odd(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))


print(filter_odd(numbers))


# * 4
def map_square(spisok):
    return list(map(lambda x: x * x, spisok))


spisok = [1, 3, 5, 7, 9]
print(map_square(spisok))


# * 5
def reduce_sum(L1):
    import functools

    return functools.reduce(lambda x, y: x + y, L1)


L1 = [1, 2, 3, 4, 50]
print(reduce_sum(L1))


# * 6
def partial_apply(func, x, y):
    def partial_func(func, x):
        return


# * 7
def apply(func, x):  #  ? higher order function
    return func(x)


def square(n):  # ?  function to be passed
    return n * n


def прибавить_один(x):
    return x + 1


def применить_операцию(список, операция):
    результат = []
    for элемент in список:
        результат.append(операция(элемент))
    return результат


числа = [1, 2, 3]
новые_числа = применить_операцию(числа, прибавить_один)
print(новые_числа)  # Выведет: [2, 3, 4]


# ? из интернета
def counter(start=0):  # higher order function
    count = start

    def increment():  # inner function
        nonlocal count  # retains access to 'count' even after counter() ends
        count += 1
        return count

    return increment  # returns the inner function


counter1 = counter(5)  # closure retains count = 5
print(counter1())
print(counter1())

counter2 = counter(10)  # new closure with count = 10
print(counter2())


def compose(f, g, arg):
    h = g(f(arg))
    return h


l = [1, 2, 3, 4, 5]

# g = filter(x % 2 == 0, l)
f = lambda x: x**2
print(f(l))


# * 8
def create_function_with_arguments(func, *arguments): ...
