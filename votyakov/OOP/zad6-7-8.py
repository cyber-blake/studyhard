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
# f = lambda x: x**2
# print(f(l))


# * 8
def create_function_with_arguments(func, *arguments): ...
