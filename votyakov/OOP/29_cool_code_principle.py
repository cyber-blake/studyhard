#
# * 1
"""ОТВЕТ: В этом примере класс  Employee имеет несколько методов,
которые относятся к разным ответственностям:  display_info
отображает информацию о сотруднике,  generate_email
генерирует электронную почту сотрудника,  send_email
отправляет электронную почту.
Такой подход не соответствует принципу единственной ответственности, так
как класс  Employee  выполняет сразу несколько различных
функций. Это делает класс менее модульным и сложным для поддержки и
тестирования.
"""


class Employee:
    def __init__(self, name, employee_id, position, mail):
        self.name = name
        self.employee_id = employee_id
        self.position = position
        self.mail = mail

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")
        print(f"Mail: {self.mail}")


class EmailService:

    @staticmethod
    def generate_email(employee):
        return f"{employee.name.lower().replace(' ', '.')}.{employee.employee_id}@company.com"

    @staticmethod
    def send_email(recipient, subject, message):
        print(f"Sending email to {recipient}:\nSubject: {subject}\nMessage: {message}")


# * 2
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == "FAV":
            return self.price * 0.2


class VipDiscount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == "VIP":
            return self.price * 0.4


# * 3
class Shape:
    def area(self):
        raise NotImplementedError("Метод area() должен быть реализован в подклассе")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

    def __str__(self):
        return f"Square({self.side})"


def calculate_total_area(shapes):
    """Вычисляет общую площадь всех фигур в списке"""
    total_area = 0
    for shape in shapes:
        total_area += shape.area()
    return total_area


# Пример использования
if __name__ == "__main__":
    # Создаем фигуры
    rectangle = Rectangle(4, 5)
    square = Square(3)

    print(f"Площадь прямоугольника: {rectangle.area()}")  # 20
    print(f"Площадь квадрата: {square.area()}")  # 9

    # Вычисляем общую площадь
    total = calculate_total_area([rectangle, square])
    print(f"Общая площадь: {total}")  # 29

    # Демонстрация полиморфизма
    shapes = [Rectangle(2, 3), Square(4), Rectangle(5, 2), Square(6)]

    print("\nВсе фигуры:")
    for i, shape in enumerate(shapes, 1):
        print(f"{i}. {shape}: площадь = {shape.area()}")

    print(f"\nОбщая площадь всех фигур: {calculate_total_area(shapes)}")
# * 4
from abc import ABC, abstractmethod


class Walker(ABC):
    @abstractmethod
    def walk(self):
        pass


class Swimmer(ABC):
    @abstractmethod
    def swim(self):
        pass


class Flyer(ABC):
    @abstractmethod
    def fly(self):
        pass


class Bird(ABC):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Crow(Bird, Walker, Flyer):

    def walk(self):
        return f"{self.name} ходит вразвалочку"

    def fly(self):
        return f"{self.name} летает высоко в небе"


class Penguin(Bird, Walker, Swimmer):

    def walk(self):
        return f"{self.name} ходит вперевалку"

    def swim(self):
        return f"{self.name} отлично плавает в холодной воде"


# * 5
from abc import ABC, abstractmethod


class Device(ABC):
    """Абстрактный интерфейс для всех устройств умного дома"""

    @abstractmethod
    def turn_on(self):
        """Включить устройство"""
        pass

    @abstractmethod
    def turn_off(self):
        """Выключить устройство"""
        pass


class Lamp(Device):
    """Класс Лампы"""

    def __init__(self, name="Лампа"):
        self.name = name
        self.is_on = False
def turn_on(self):
        self.is_on = True
        print(f"{self.name} включена")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} выключена")

    def __str__(self):
        return f"{self.name} ({'вкл' if self.is_on else 'выкл'})"


class MotionSensor(Device):
    """Класс Датчика движения"""

    def __init__(self, name="Датчик движения"):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} активирован")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} деактивирован")

    def detect_motion(self):
        """Дополнительный метод, специфичный для датчика движения"""
        if self.is_on:
            print(f"{self.name} обнаружил движение!")
        else:
            print(f"{self.name} выключен, не может обнаружить движение")

    def __str__(self):
        return f"{self.name} ({'активен' if self.is_on else 'неактивен'})"


class Thermostat(Device):
    """Класс Термостата"""

    def __init__(self, name="Термостат", temperature=20):
        self.name = name
        self.is_on = False
        self.temperature = temperature

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} включен, текущая температура: {self.temperature}°C")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} выключен")

    def set_temperature(self, temp):
        """Дополнительный метод для установки температуры"""
        if self.is_on:
            self.temperature = temp
            print(f"{self.name} установлена температура: {temp}°C")
        else:
            print(f"{self.name} выключен, нельзя установить температуру")

    def __str__(self):
        return f"{self.name} ({self.temperature}°C, {'вкл' if self.is_on else 'выкл'})"


class SmartHome:
    """Умный дом, управляющий устройствами через абстракцию Device"""

    def __init__(self, devices=None):
        # SmartHome зависит от абстракции Device, а не от конкретных классов
        self.devices = devices if devices else []

    def add_device(self, device: Device):
        """Добавить устройство в умный дом"""
        self.devices.append(device)
        print(f"Добавлено устройство: {device}")

    def remove_device(self, device: Device):
        """Удалить устройство из умного дома"""
        if device in self.devices:
            self.devices.remove(device)
            print(f"Удалено устройство: {device}")

    def turn_on(self):
        """Включить все устройства"""
        print("🔌 ВКЛЮЧЕНИЕ ВСЕХ УСТРОЙСТВ:")
        for device in self.devices:
            device.turn_on()
        print()

    def turn_off(self):
        """Выключить все устройства"""
        print("🔌 ВЫКЛЮЧЕНИЕ ВСЕХ УСТРОЙСТВ:")
        for device in self.devices:
            device.turn_off()
        print()

    def turn_on_selected(self, device_names):
        """Включить выбранные устройства по имени"""
        print(f"🔌 ВКЛЮЧЕНИЕ УСТРОЙСТВ: {device_names}")
        for device in self.devices:
            if any(name in str(device) for name in device_names):
                device.turn_on()
        print()

    def get_status(self):
        """Получить статус всех устройств"""
        print("📊 СТАТУС УСТРОЙСТВ:")
        for i, device in enumerate(self.devices, 1):
            print(f"  {i}. {device}")
        print()


# Дополнительные устройства (легко расширяемо)
class SmartTV(Device):
    """Умный телевизор"""

    def __init__(self, name="Умный телевизор"):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} включен")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} выключен")

    def __str__(self):
        return f"{self.name} ({'вкл' if self.is_on else 'выкл'})"


class SecurityCamera(Device):
    """Камера безопасности"""

    def __init__(self, name="Камера безопасности"):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} активирована, ведется наблюдение")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} деактивирована")

    def __str__(self):
        return f"{self.name} ({'активна' if self.is_on else 'неактивна'})"


# Основная программа
if __name__ == "__main__":
    print("🏠 СИСТЕМА УМНОГО ДОМА\n")

    # Создаем устройства
    lamp = Lamp("Гостинная лампа")
    motion_sensor = MotionSensor("Прихожая датчик")
    thermostat = Thermostat("Котел", 22)
    tv = SmartTV("Samsung TV")
    camera = SecurityCamera("Уличная камера")

    # Создаем умный дом
    smart_home = SmartHome([lamp, motion_sensor, thermostat])

    # Добавляем дополнительные устройства
    smart_home.add_device(tv)
    smart_home.add_device(camera)

    # Показываем начальный статус
    smart_home.get_status()

    # Включаем все устройства
    smart_home.turn_on()

    # Используем специфичные методы устройств
    motion_sensor.detect_motion()
    thermostat.set_temperature(24)

    print()
    smart_home.get_status()

    # Выключаем все устройства
    smart_home.turn_off()

    # Включаем только выбранные устройства
    smart_home.turn_on_selected(["лампа", "телевизор"])
# * 6
from abc import ABC, abstractmethod
from typing import Optional


class Transferable(ABC):
    """Интерфейс для объектов, поддерживающих переводы"""

    @abstractmethod
    def transfer(self, amount: float, target_account: "Account") -> bool:
        pass


class AccountInterface(ABC):
    """Базовый интерфейс для всех счетов"""

    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> bool:
        pass

    @abstractmethod
    def get_balance(self) -> float:
        pass


class Account(AccountInterface, Transferable):
    """Базовый класс банковского счета"""

    def __init__(self, account_number: str, balance: float = 0.0):
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
            print(f"Внесено {amount:.2f} на счет {self._account_number}")
        else:
            raise ValueError("Сумма должна быть положительной")

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")

        if self._balance >= amount:
            self._balance -= amount
            print(f"Снято {amount:.2f} со счета {self._account_number}")
            return True
        else:
            print(f"Недостаточно средств на счете {self._account_number}")
            return False

    def get_balance(self) -> float:
        return self._balance

    def transfer(self, amount: float, target_account: "Account") -> bool:
        """Перевод средств на другой счет"""
        if not isinstance(target_account, Account):
            raise TypeError("Целевой счет должен быть экземпляром Account")

        print(
            f"Попытка перевода {amount:.2f} с {self._account_number} на {target_account._account_number}"
        )

        if self.withdraw(amount):
            target_account.deposit(amount)
            print(f"✅ Перевод успешно завершен")
            return True
        else:
            print(f"❌ Перевод отменен: недостаточно средств")
            return False

    def get_account_number(self) -> str:
        return self._account_number

    def __str__(self):
        return f"Счет {self._account_number}: {self._balance:.2f}"


class SavingsAccount(Account):

    def __init__(
        self, account_number: str, balance: float = 0.0, interest_rate: float = 0.0
    ):
        super().__init__(account_number, balance)
        self._interest_rate = interest_rate

    def calculate_interest(self) -> float:
        """Рассчитать проценты по счету"""
        interest = self._balance * (self._interest_rate / 100)
        print(f"Начислены проценты: {interest:.2f}")
        return interest

    def get_interest_rate(self) -> float:
        return self._interest_rate

    def apply_interest(self) -> None:
        """Применить проценты к балансу"""
        interest = self.calculate_interest()
        self.deposit(interest)

    def __str__(self):
        return f"Сберегательный {super().__str__()}, ставка: {self._interest_rate}%"


class CheckingAccount(Account):
    """Текущий счет с комиссиями"""

    def __init__(
        self, account_number: str, balance: float = 0.0, fee_percentage: float = 0.0
    ):
        super().__init__(account_number, balance)
        self._fee_percentage = fee_percentage

    def deduct_fees(self) -> None:
        """Вычесть комиссию"""
        fee = self._balance * (self._fee_percentage / 100)
        if self.withdraw(fee):
            print(f"Списана комиссия: {fee:.2f}")

    def get_fee_percentage(self) -> float:
        return self._fee_percentage

    def __str__(self):
        return f"Текущий {super().__str__()}, комиссия: {self._fee_percentage}%"


class TransferService:
    """Сервис для выполнения операций перевода между счетами"""

    @staticmethod
    def execute_transfer(source: Transferable, target: Account, amount: float) -> bool:
        """Выполнить перевод между счетами"""
        if not isinstance(source, Transferable):
            raise TypeError(
                "Источник перевода должен поддерживать интерфейс Transferable"
            )

        if amount <= 0:
            raise ValueError("Сумма перевода должна быть положительной")

        print(f"\n🔄 ИНИЦИИРОВАН ПЕРЕВОД:")
        print(f"   От: {source}")
        print(f"   Кому: {target}")
        print(f"   Сумма: {amount:.2f}")

        success = source.transfer(amount, target)

        if success:
            print("✅ Перевод успешно выполнен")
        else:
            print("❌ Перевод не выполнен")

        return success

    @staticmethod
    def bulk_transfer(transfers: list) -> dict:
        """Выполнить несколько переводов"""
        results = {"successful": 0, "failed": 0, "details": []}

        for source, target, amount in transfers:
            try:
                success = TransferService.execute_transfer(source, target, amount)
                if success:
                    results["successful"] += 1
                else:
                    results["failed"] += 1
                results["details"].append(
                    {
                        "source": source.get_account_number(),
                        "target": target.get_account_number(),
                        "amount": amount,
                        "success": success,
                    }
                )
            except Exception as e:
                results["failed"] += 1
                results["details"].append(
                    {
                        "source": source.get_account_number(),
                        "target": target.get_account_number(),
                        "amount": amount,
                        "success": False,
                        "error": str(e),
                    }
                )

        return results


class Bank:
    """Банк, управляющий счетами"""

    def __init__(self):
        self._accounts = {}
        self._transfer_service = TransferService()

    def add_account(self, account: Account) -> None:
        """Добавить счет в банк"""
        self._accounts[account.get_account_number()] = account
        print(f"✅ Добавлен счет: {account}")

    def remove_account(self, account_number: str) -> bool:
        """Удалить счет из банка"""
        if account_number in self._accounts:
            account = self._accounts.pop(account_number)
            print(f"✅ Удален счет: {account}")
            return True
        return False

    def get_account(self, account_number: str) -> Optional[Account]:
        """Найти счет по номеру"""
        return self._accounts.get(account_number)

    def transfer_funds(
        self, source_account_number: str, destination_account_number: str, amount: float
    ) -> bool:
        """Перевести средства между счетами"""
        source = self.get_account(source_account_number)
        destination = self.get_account(destination_account_number)

        if not source:
            raise ValueError(f"Счет-источник {source_account_number} не найден")
        if not destination:
            raise ValueError(f"Счет-получатель {destination_account_number} не найден")
        if source == destination:
            raise ValueError("Нельзя переводить средства на тот же счет")

        return self._transfer_service.execute_transfer(source, destination, amount)

    def get_total_balance(self) -> float:
        """Общий баланс всех счетов"""
        return sum(account.get_balance() for account in self._accounts.values())

    def display_accounts(self) -> None:
        """Показать все счета"""
        print("\n📊 ВСЕ СЧЕТА В БАНКЕ:")
        for account in self._accounts.values():
            print(f"   {account}")
        print(f"   ИТОГО: {self.get_total_balance():.2f}")

        # Дополнительный класс для демонстрации расширяемости


class BusinessAccount(Account):
    """Бизнес-счет с дополнительными функциями"""

    def __init__(
        self, account_number: str, balance: float = 0.0, credit_limit: float = 0.0
    ):
        super().__init__(account_number, balance)
        self._credit_limit = credit_limit

    def withdraw(self, amount: float) -> bool:
        """Снятие с учетом кредитного лимита"""
        available_funds = self._balance + self._credit_limit
        if amount <= available_funds:
            self._balance -= amount
            print(f"Снято {amount:.2f} со счета {self._account_number}")
            return True
        return False

    def __str__(self):
        return f"Бизнес {super().__str__()}, кредитный лимит: {self._credit_limit:.2f}"


# Основная программа
if __name__ == "__main__":
    print("🏦 СИСТЕМА УПРАВЛЕНИЯ БАНКОВСКИМИ СЧЕТАМИ\n")

    # Создаем счета
    savings_account = SavingsAccount(
        account_number="SAV-001", balance=1000, interest_rate=5
    )
    checking_account = CheckingAccount(
        account_number="CHK-001", balance=500, fee_percentage=2
    )
    business_account = BusinessAccount(
        account_number="BUS-001", balance=2000, credit_limit=1000
    )

    # Создаем банк и добавляем счета
    bank = Bank()
    bank.add_account(savings_account)
    bank.add_account(checking_account)
    bank.add_account(business_account)

    # Показываем начальные балансы
    print("\n💰 НАЧАЛЬНЫЕ БАЛАНСЫ:")
    print(f"Сберегательный счет: {savings_account.get_balance():.2f}")
    print(f"Текущий счет: {checking_account.get_balance():.2f}")
    print(f"Бизнес счет: {business_account.get_balance():.2f}")

    # Выполняем перевод
    bank.transfer_funds(
        source_account_number="SAV-001",
        destination_account_number="CHK-001",
        amount=500,
    )

    # Показываем обновленные балансы
    print("\n💰 ОБНОВЛЕННЫЕ БАЛАНСЫ:")
    print(f"Сберегательный счет: {savings_account.get_balance():.2f}")
    print(f"Текущий счет: {checking_account.get_balance():.2f}")

    # Демонстрация дополнительных функций
    print("\n🎯 ДОПОЛНИТЕЛЬНЫЕ ОПЕРАЦИИ:")
    savings_account.apply_interest()
    checking_account.deduct_fees()

    # Показываем все счета
    bank.display_accounts()

    # Демонстрация массовых переводов
    print("\n🔄 МАССОВЫЕ ПЕРЕВОДЫ:")
    transfers = [
        (savings_account, checking_account, 100),
        (business_account, savings_account, 300),
        (checking_account, business_account, 50),
    ]

    results = TransferService.bulk_transfer(transfers)
    print(f"Успешных переводов: {results['successful']}")
    print(f"Неудачных переводов: {results['failed']}")

    # Финальный статус
    bank.display_accounts()
