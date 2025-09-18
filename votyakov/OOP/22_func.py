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
        return partial_func


# * 7
def compose(f, g):

    def h(x):
        return g(f(x))

    return h


add_one = lambda x: x + 1
multiply_by_two = lambda x: x * 2

composed_function = compose(add_one, multiply_by_two)

print(f"Результат композиции: {composed_function(5)}")


# * 8
def create_function_with_arguments(func, arguments):

    def new_func():
        return func(*arguments)

    return new_func


def sum_numbers(a, b, c):
    return a + b + c


args = [10, 20, 30]
sum_with_args = create_function_with_arguments(sum_numbers, args)

print(f"Результат: {sum_with_args()}")


# * 9
def compose_functions(functions):

    def composed_function(x):
        result = x
        for func in functions:
            result = func(result)
        return result

    return composed_function


add_five = lambda x: x + 5
square = lambda x: x**2
subtract_three = lambda x: x - 3

function_list = [add_five, square, subtract_three]
final_function = compose_functions(function_list)

print(f"Результат композиции списка функций: {final_function(2)}")
