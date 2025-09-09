# * 1
def calc(str):
    a, b, op = str.split()
    a = float(a)
    b = float(b)
    try:
        return a / b
    except ZeroDivisionError:
        return "ERROR"


print(calc(input()))


# * 2
def filter_hex_string(string):
    try:
        int(string, 16)
        return True
    except ValueError:
        return False


# задача: чтобы в список попадали те строки, которые проходят фильтр
# для этого нужно подать список строк, -> разбив одну строку через пробел
def check_password(*args):
    args = list(args)
    args = args.split()
    return filter(filter_hex_string, args)


# print(list(check_password(input())))


# * 3
olympiad1 = {
    "name": "Пробная вышка",
    "winners": {
        "Олеся Олимпиадникova": 594,
        "Олег Олимпиадников": 587,
        "Онисим Олимпиадников": 581,
    },
}

olympiad2 = {
    "name": "Горные воробьи",
    "winners": {
        "Ольга Олимпиадникова": (20, 20, 19, 20),
        "Олеся Олимпиадникова": (19, 19, 20, 20, 17),
        "Офелия Олимпиадникова": (20, 20, 20, 20, 13),
    },
}


def checkOlympiads(name):
    try:
        points1 = olympiad1["winners"][name]
        print(f'[{olympiad1["name"]}] победитель {points1}')
    except KeyError:
        print(f'[{olympiad1["name"]}] призёр')
    finally:
        print()
    try:
        points2 = olympiad2["winners"][name][4]
        print(f"[{olympiad2['name']}] победитель {points2}")
    except IndexError:
        print(f"[{olympiad2['name']}] победитель")
    except KeyError:
        print(f"[{olympiad2['name']}] призёр")
    finally:
        print()


checkOlympiads("Ольга Олимпиадникова")
checkOlympiads("Олеся Олимпиадникова")


# *4
def terribly_impolite_program():
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Ты не пройдёшь!")
        terribly_impolite_program()


terribly_impolite_program()


# * 5
class LizardInGlassError(Exception):
    """Исключение для ящерицы в стакане"""

    pass


class ToiletQuestionError(Exception):
    """Исключение для вопроса о туалете"""

    pass


class BarOnFireError(Exception):
    """Исключение для возгорания бара"""

    pass


class NegativeOrderError(Exception):
    """Исключение для отрицательного заказа"""

    pass


def process_order(order):
    """Обрабатывает заказ в баре"""

    try:
        # Проверяем специальные случаи
        if "ящериц" in order.lower() or "lizard" in order.lower():
            raise LizardInGlassError("Мы не подаем ящериц в стакане!")

        if "туалет" in order.lower() or "toilet" in order.lower():
            raise ToiletQuestionError("Клиент спрашивает про туалет!")

        if "qwerty" in order.lower():
            raise ValueError("Некорректный заказ: qwerty")

        # Извлекаем количество из заказа
        import re

        match = re.search(r"(-?\d+)", order)

        if match:
            quantity = int(match.group(1))

            # Проверяем отрицательное количество
            if quantity < 0:
                raise NegativeOrderError("Нельзя заказать отрицательное количество!")

            # Проверяем разумные пределы
            assert quantity <= 1000, f"Слишком большой заказ: {quantity} кружек"
            assert quantity >= 0, "Количество не может быть отрицательным"

            return f"Приготовлено {quantity} кружек лимонада"

        else:
            raise ValueError("Не могу распознать количество в заказе")

    except LizardInGlassError as e:
        return f"Ошибка: {e}"

    except NegativeOrderError as e:
        return f"Ошибка: {e}"

    except ToiletQuestionError:
        # Это вызовет пожар в finally блоке
        raise BarOnFireError("Бар вспыхивает пламенем от вопроса о туалете!")

    except ValueError as e:
        return f"Ошибка заказа: {e}"

    except AssertionError as e:
        return f"Недопустимый заказ: {e}"

    finally:
        print(f"Обработан заказ: '{order}'")


def bar_scenario():
    """Сценарий из анекдота"""

    orders = [
        "кружку лимонада",
        "2 кружки лимонада",
        "0 кружек лимонада",
        "999999999 кружек лимонада",
        "ящерицу в стакане",
        "-1 кружку лимонада",
        "qwerty кружек лимонада",
    ]

    print("Тестировщик заходит в бар и заказывает:\n")

    for order in orders:
        try:
            result = process_order(order)
            print(f"✓ {result}")
        except BarOnFireError as e:
            print(f"🔥 {e}")
            break
        except Exception as e:
            print(f"✗ Неожиданная ошибка: {e}")
        print()

    # Первый реальный клиент
    print("Первый реальный клиент заходит в бар:")
    try:
        process_order("где туалет")
    except BarOnFireError as e:
        print(f"🔥 {e}")
    finally:
        print("Сценарий завершен!")


# Запуск сценария
if __name__ == "__main__":
    bar_scenario()
