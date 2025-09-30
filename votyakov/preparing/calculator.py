def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    try:
        res = x / y
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Can only take numbers"
    else:
        return res
