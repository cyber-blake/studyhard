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


# planet1 = Planet("Земля", 4540, "16.92", 6371, "29.8")
# star1 = Star("Полярная звезда", 60, "5500", 47, "Малая Медведица")
# print(Planet.__doc__, end="\n")
# planet1.display()
# print(Star.__doc__, end="\n")
# star1.display()
# ! раскоментит перед сдачей

# * 2
from datetime import datetime, date, time, timedelta


class Pastry:  # ? родительский класс
    def __init__(self, name, price, manufacture_date, term) -> None:
        self.name = name
        self.price = price
        self.manufacture_date = manufacture_date
        self.term = term  # days of storage

    def display(self):
        print(
            f"Наименование: {self.name}\nЦена: {self.price} \nДата изготвления: {self.manufacture_date}"
        )

    def valid_until(self):
        """Вычисляет количество дней до истечения срока годности"""
        # Если manufacture_date уже datetime объект - используем напрямую
        expiration_date = self.manufacture_date + timedelta(days=self.term)
        current_date = datetime.now()
        days_until_expiration = (expiration_date - current_date).days
        return days_until_expiration


class Cake(Pastry):  # ? дочерний класс 1
    def __init__(self, name, price, manufacture_date, term, filling) -> None:
        super().__init__(name, price, manufacture_date, term)
        self.filling = filling

    def display(self):
        print(
            f"Название: {self.name}\nЦена: {self.price} \nДата изготвления: {self.manufacture_date}\nНачинка: {self.filling}\nСрок годности истекает через {self.valid_until()} дней"
        )

    def order(self):
        self.display()
        if self.valid_until() >= 0:
            print(f"Оформлен заказ {id(self)} - {self.name} с начинкой {self.filling}")
        else:
            print("К сожалению, выпечка просрочена...")


class BentoCake(Pastry):  # ? дочерний класс 2
    def __init__(self, name, price, manufacture_date, term, celebration) -> None:
        super().__init__(name, price, manufacture_date, term)
        self.celebration = celebration

    def display(self):
        print(
            f"Название: {self.name}\nЦена: {self.price} \nДата изготвления: {self.manufacture_date}\nПраздник: {self.celebration}\nСрок годности истекает через {self.valid_until()} дней"
        )

    def order(self):
        self.display()
        if self.valid_until() >= 0:
            print(f"Оформлен заказ {id(self)} - {self.name} на {self.celebration}")
        else:
            print("К сожалению, выпечка просрочена...")


cake1 = Cake("Торт", 1300, datetime(2025, 9, 24), 3, "вишня")
bento1 = BentoCake("Бенто торт", 1000, datetime(2025, 10, 20), 4, "день рождения")

# cake1.order()
# print()
# bento1.order()


# * 3
# Создайте базовый класс `BankAccount`, который:
# - содержит конструктор, инициализирующий атрибуты Банковских аккаунтов:
# приватный атрибут: `holder` (владелец), публичные: `balance` и
# `interest_rate` (баланс и процентная ставка);
# - содержит getter и setter для приватного атрибута;
# - переопределяет магический метод `__str__()`.
# Затем добавьте дочерний класс `BankOperation`, который наследует все
# свойства и методы от класса `BankAccount`, и кроме того, имеет свои
# методы и атрибуты:
# - `deposit(amount)` добавляет сумму к балансу и регистрирует транзакцию;
# - `withdraw(amount)` вычитает сумму из баланса и записывает транзакцию;
# - `add_interest()` добавляет проценты к счету на основе `interest_rate` и
# записывает транзакцию
# - `history()` печатает список всех операций по счету.
class BankAccount:
    def __init__(self, holder, balance, interest_rate) -> None:
        self.__holder = holder
        self.balance = balance
        self.interest_rate = interest_rate

    @property
    def holder(self):
        return self.__holder

    @holder.setter
    def holder(self, new_holder):
        self.__holder = new_holder

    def __str__(self) -> str:
        return f"Информация по счёту {id(self)}\nВладелец счёта: {self.__holder}\nОстаток по счёту {self.balance:,.2f} $\nПроцентная ставка {self.interest_rate}"


class BankOperation(BankAccount):
    def __init__(self, holder, balance, interest_rate):
        super().__init__(holder, balance, interest_rate)
        self.op_history = []

    def deposit(self, amount):  # добавляет сумму к балансу и регистрирует транзакцию;
        self.balance += amount
        self.op_history.append(
            f"Аккаунт {id(self)} - внесение наличных на счет: ${amount:,.2f}"
        )

    # ? :,.2f
    def withdraw(self, amount):  # вычитает сумму из баланса и записывает транзакцию;
        self.balance -= amount
        self.op_history.append(f"Аккаунт {id(self)} - cнятие наличных: ${amount:,.2f}")

    def add_interest(
        self,
    ):
        self.op_history.append(
            f"Аккаунт {id(self)} - начислены проценты по вкладу: ${self.balance * self.interest_rate:,.2f} "
        )
        # - `add_interest()` добавляет проценты к счету на основе `interest_rate` и записывает транзакцию

    def history(self):  # - `history()` печатает список всех операций по счет
        print(*self.op_history, sep="\n")


account = BankOperation("Warren Buffett", 113000000000, 0.08)
account.__str__()
account.deposit(4000000000)
account.withdraw(88000000000)
account.add_interest()
account.history()
print(account)

# * 4
class ComputerDevice:
    '''Request process'''
    def __init__(self, inf):
        print('Start init ComputerDevice.__init__()')
        self.inf = inf
        print('End init ComputerDevice.__init__()')
class Scanner(ComputerDevice):
    '''Scan information'''
    def __init__(self, inf):
        print('Start init Scanner.__init__()')
        super().__init__(inf)
        print('End init Scanner.__init__()')
class Printer(ComputerDevice):
    '''Print information'''
    def __init__(self, inf):
        print('Start init Printer.__init__()')
        super().__init__(inf)
        print('End init Printer.__init__()')
    class Copier(Scanner, Printer):
    '''Copy process'''
    def __init__(self, inf):
        print('Start init Copier.__init__()')
        super().__init__(inf)
        print(f'Отсканированная информация: {self.inf.upper()}')
        print('End init Copier.__init__()')
        print(Copier.__mro__)

c = Copier('Hello world!')
