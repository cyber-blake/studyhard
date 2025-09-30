import math


def circle(r=5):
    return (
        f"Площадь окружности = {math.pi * (r**2)}, длина окружности = {math.pi * r * 2}"
    )


def triangle(a=7, b=2, c=8):
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Треугольник с такими сторонами не существует")
    else:
        p = (a + b + c) / 2
        return f"Периметр треугольника = {p*2}, площадь треугольника = {math.sqrt(p * (p - a) * (p - b) * (p - c)):.2f}"


def square(a=15):
    return f"Периметр квадрата = {a*4}, площадь квадрата = {a**2}"
