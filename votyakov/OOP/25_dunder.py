#
# * 1
class SignedMessage:
    """
    `message` - сообщение, представленное строкой, а
    `signature`- очень крутая подпись
    """

    def __init__(self, message, signature) -> None:
        self.message = message
        self.signature = signature

    def __str__(self) -> str:
        return f"{self.message} {self.signature}"

    def __add__(self, other) -> str:
        return f"{self.message} {other}"


SIGNATURE = "-~=$([{PETR}])$=~-"

# выводится "Hello -~=$([{PETR}])$=~-"
print(SignedMessage("Hello ", SIGNATURE))

# выводится "world! -~=$([{PETR}])$=~-"
print(SignedMessage("world!", SIGNATURE))

# выводится "Hello world! -~=$([{PETR}])$=~-"
print(SignedMessage("Hello ", SIGNATURE) + SignedMessage("world!", SIGNATURE))
# * 2


class Vector2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Vector3:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return (-self.x, -self.y, -self.z)

    def __abs__(self):
        import math

        x = self.x**2 + self.y**2 + self.z**2
        return int(math.sqrt(x))

    def __str__(self) -> str:
        t = {self.x, self.y, self.z}
        return f"{t}"


a = Vector3(1, -2, 3)
b = Vector3(3, 4, 5)
print(a - b)
print(a + b)
c = Vector3(1, 0, -1)
print(-c)
d = Vector3(3, 4, 0)
print(abs(d))
print(d)

# * 3
from enum import Enum
from functools import total_ordering


class Rarity(Enum):
    COMMON = 0
    RARE = 1
    EPIC = 2
    LEGENDARY = 3


@total_ordering
class Item:
    def __init__(self, ID, price, rarity, color):
        self.ID = ID
        self.price = price
        # Преобразуем числовую редкость в enum, если нужно
        if isinstance(rarity, int):
            self.rarity = Rarity(rarity)
        else:
            self.rarity = rarity
        self.color = (
            color.upper() if color else "000000"
        )  # Нормализуем к верхнему регистру

    def __repr__(self):
        return f"Item(ID={self.ID}, price={self.price}, rarity={self.rarity.name}, color='{self.color}')"

    def _key(self):
        """Вспомогательный метод для генерации ключа сравнения"""
        # Для цвета: преобразуем hex в числовое значение для правильного сравнения
        # Более высокое числовое значение = более светлый цвет
        color_value = int(self.color, 16) if self.color else 0

        return (
            self.ID,  # по возрастанию
            self.price,  # по возрастанию
            -self.rarity.value,  # по убыванию (отрицание дает обратный порядок)
            -color_value,  # по убыванию насыщенности
        )

    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self._key() == other._key()

    def __lt__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self._key() < other._key()


# Создаем тестовые данные для проверки
items = [
    Item(128, 500, 1, "FF5819"),  # Редкий, оранжевый
    Item(128, 500, 1, "FF5820"),  # Редкий, чуть другой оттенок
    Item(128, 500, 2, "FF5819"),  # Эпический, оранжевый
    Item(128, 600, 1, "FF5819"),  # Дороже
    Item(129, 500, 1, "FF5819"),  # Другой ID
    Item(127, 500, 3, "FFFFFF"),  # Легендарный, белый
    Item(127, 500, 3, "000000"),  # Легендарный, черный
    Item(127, 400, 3, "FF0000"),  # Легендарный, красный (дешевле)
]

print("До сортировки:")
for item in items:
    print(item)

print("\nПосле сортировки:")
items.sort()
for item in items:
    print(item)

# Дополнительная проверка операторов сравнения
print("\nПроверка операторов сравнения:")
item1 = Item(100, 500, 1, "FF0000")
item2 = Item(100, 500, 2, "FF0000")
item3 = Item(100, 500, 1, "FF0000")

print(f"item1 == item3: {item1 == item3}")
print(f"item1 != item2: {item1 != item2}")
print(f"item1 < item2: {item1 < item2}")
print(f"item2 > item1: {item2 > item1}")
print(f"item1 <= item3: {item1 <= item3}")
print(f"item2 >= item1: {item2 >= item1}")
