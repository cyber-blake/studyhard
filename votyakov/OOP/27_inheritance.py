#
# * 1
class HeavenlyBody:
    """
    Родительский класс HeavenlyBody
    """

    def __init__(self, name, age, temp, raduis) -> None:
        self.name = name
        self.age = age
        self.temperature = temp
        self.raduis = raduis

    def display(self):
        print(self.name, self.age, self.temperature, self.temperature)


class Planet(HeavenlyBody):
    """Дочерний класс Planet"""

    def __init__(self, name, age, temp, raduis, orbital_speed) -> None:
        super().__init__(name, age, temp, raduis)
        self.orbital_speed = orbital_speed

    def display(self):
        print(
            f"Название: {self.name}\nВозраст: {self.age} (млн.лет) \nТемпература: {self.temperature} (С)\nРадиус: {self.raduis} (км) \nОрбитальная скорость: {self.orbital_speed}(км/с)"
        )


class Star(HeavenlyBody):
    """
    Дочерний класс Planet"""

    def __init__(self, name, age, temp, raduis, constellation) -> None:
        super().__init__(name, age, temp, raduis)
        self.constellation = constellation

    def display(self):
        print(
            f"Название: {self.name}\nВозраст: {self.age} (млн.лет) \nТемпература: {self.temperature} (С)\nРадиус: {self.raduis} (км) \nСозвездие: {self.constellation}\n"
        )


planet1 = Planet("Земля", 4540, "16.92", 6371, "29.8")
star1 = Star("Полярная звезда", 60, "5500", 47, "Малая Медведица")
print(Planet.__doc__, end="\n")
planet1.display()
print(Star.__doc__, end="\n")
star1.display()


# * 2
import datetime


class Pastry:  # ? родительский класс
    def __init__(self, name, price, manufacture_date, term) -> None:
        self.name = name
        self.price = price
        self.manufacture_date = manufacture_date
        self.term = term

    def display(self):
        print(
            f"Наименование: {self.name}\nЦена: {self.price} \nДата изготвления: {self.manufacture_date}\nСрок хранения: {self.term}"
        )

    def valid_until(self):
        """который позволяет вычислить количество дней до
        истечения срока годности рассматриваемого изделия"""
        ...


class Cake(Pastry):  # ? дочерний класс 1
    def __init__(self, name, price, manufacture_date, term, filling) -> None:
        super().__init__(name, price, manufacture_date, term)
        self.filling = filling
        self.days = 7  # ! не забыть записать

    def display(self):
        print(
            f"Название: {self.name}\nЦена: {self.price} \nДата изготвления: {self.manufacture_date}\nНачинка: {self.filling}\nСрок годности истекает через {self.days} дней\n"
        )

    def order(self): ...


class BentoCake(Pastry):  # ? дочерний класс 2
    def __init__(self, name, price, manufacture_date, term, celebration) -> None:
        super().__init__(name, price, manufacture_date, term)
        self.celebration = celebration
        self.days = 7  # ! не забыть записать

    def display(self):
        print(
            f"Название: {self.name}\nЦена: {self.price} \nДата изготвления: {self.manufacture_date}\nПраздник: {self.celebration}\nСрок годности истекает через {self.days} дней"
        )

    def order(self): ...


cake1 = Cake("Торт", 1300, datetime.date(2023, 7, 20), 3, "вишня")
bento1 = BentoCake("Бенто торт", 1000, datetime.date(2023, 7, 20), 4, "день рождения")
cake1.display()
bento1.display()

# cake1.order()
# bento1.order()
