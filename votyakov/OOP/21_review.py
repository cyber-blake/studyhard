# * 1
# * 1.1
class NumberList:
    def __init__(self, numbers):
        self.numbers = numbers

    def sum_of_squares(self):
        result = 0
        for num in self.numbers:
            result += num**2
        return result


numbers = [1, 2, 3, 4, 5]
number_list = NumberList(numbers)
total = number_list.sum_of_squares()
# print(f"Sum of squares: {total}")

# * 1.2


def sum_of_squares(numbers):
    squared_nums = map(lambda x: x**2, numbers)
    return sum(squared_nums)


numbers = [1, 2, 3, 4, 5]
total = sum_of_squares(numbers)
# print(f"Sum of squares: {total}")


# * 1.3
def sum_of_squares(numbers):
    result = 0
    for num in numbers:
        result += num**2
    return result


numbers = [1, 2, 3, 4, 5]
total = sum_of_squares(numbers)
print(f"Sum of squares: {total}")

# ответ: 231

# * 2
# ? Используя парадигму функционального программирования, напишите функцию
# ? `sum_even_numbers(numbers)`, которая принимает список чисел и возвращает
# ? сумму всех четных чисел в списке. В ответ укажите результат функции при
# ? `numbers = [14, 93, 19, 38, 18, 51, 77]"""


def sum_even_numbers(L1):
    return sum(list(filter(lambda x: x % 2 == 0, L1)))


numbers = [14, 93, 19, 38, 18, 51, 77]
print(sum_even_numbers(numbers))

# * 3
# ? Используя парадигму императивного программирования, напишите функцию
# ? `sum_even_numbers(numbers)`, которая принимает список чисел и возвращает
# ? сумму всех четных чисел в списке. В ответ укажите результат функции при
# ? `numbers = [60, 84, 9, 49, 7, 85, 38]`

numbers = [60, 84, 9, 49, 7, 85, 38]
new_list = []
s = 0
for x in numbers:
    if x % 2 == 0:
        new_list.append(x)

for y in new_list:
    s += y

print(s)
