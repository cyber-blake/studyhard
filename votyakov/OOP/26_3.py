from datetime import datetime


class Emerald:
    def __init__(self):
        self.__status = 0  # 0-не учтён, 1-учтён, 2-под спудом
        self.__price = 0

    @property
    def status(self):
        return self.__status

    def _set_status(self, new_status):
        if new_status >= self.__status:
            self.__status = new_status
        else:
            raise ValueError("Статус не может быть понижен")

    @property
    def price(self):
        return self.__price

    def _set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            raise ValueError("Цена не может быть отрицательной")

    def evaluate(self, price):
        """Оценить изумруд"""
        self._set_price(price)

    def account(self):
        """Учесть изумруд"""
        self._set_status(1)

    def store(self):
        """Отправить под спуд"""
        self._set_status(2)


class Shell:
    def __init__(self):
        self.__status = 0  # 0-не учтена, 1-учтена, 2-в отделении, 3-переплавлена
        self.__price = 0

    @property
    def status(self):
        return self.__status

    def _set_status(self, new_status):
        if new_status >= self.__status:
            self.__status = new_status
        else:
            raise ValueError("Статус не может быть понижен")

    @property
    def price(self):
        return self.__price

    def _set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            raise ValueError("Цена не может быть отрицательной")

    def evaluate(self, price):
        """Оценить скорлупку"""
        self._set_price(price)

    def account(self):
        """Учесть скорлупку"""
        self._set_status(1)

    def process(self):
        """Отправить в монетолитейное отделение"""
        self._set_status(2)

    def smelt(self):
        """Переплавить в монету"""
        self._set_status(3)


class Coin:
    def __init__(self, serial_number, year, value):
        self.__serial_number = serial_number
        self.__year = year
        self.__value = value

    @property
    def serial_number(self):
        return self.__serial_number

    @property
    def year(self):
        return self.__year

    @property
    def value(self):
        return self.__value


class Entry:
    _id_counter = 0

    def __init__(self, item, date=None, info="", secret=False):
        Entry._id_counter += 1
        self.__ID = Entry._id_counter
        self.__item = item
        self.__date = date if date else datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        self.__info = info
        self.__secret = secret

    @property
    def ID(self):
        return self.__ID

    @property
    def item(self):
        return self.__item

    @property
    def date(self):
        return self.__date

    @property
    def info(self):
        return self.__info

    @info.setter
    def info(self, new_info):
        self.__info = new_info

    @property
    def secret(self):
        return self.__secret

    def classify(self):
        """Засекретить запись"""
        self.__secret = True

    def declassify(self):
        """Рассекретить запись"""
        self.__secret = False

    def __str__(self):
        item_type = type(self.__item).__name__
        secret_status = "🔒" if self.__secret else "🔓"
        return f"{secret_status} Запись #{self.__ID}: {item_type} ({self.__date})"


class Archive:
    def __init__(self):
        self.__storage = []

    def add(self, entry):
        """Добавить запись в архив"""
        if not isinstance(entry, Entry):
            raise ValueError("Можно добавлять только объекты Entry")
        self.__storage.append(entry)

    def get(self, index):
        """Получить информацию о записи по индексу"""
        if index < 0 or index >= len(self.__storage):
            return None

        entry = self.__storage[index]

        # Проверка на удаленную или засекреченную запись
        if entry is None or entry.secret:
            return None

        # Получаем информацию об объекте
        item = entry.item
        item_info = {}

        if isinstance(item, Emerald):
            item_info = {"type": "Emerald", "status": item.status, "price": item.price}
        elif isinstance(item, Shell):
            item_info = {"type": "Shell", "status": item.status, "price": item.price}
        elif isinstance(item, Coin):
            item_info = {
                "type": "Coin",
                "serial_number": item.serial_number,
                "year": item.year,
                "value": item.value,
            }

        return {
            "entry_id": entry.ID,
            "entry_date": entry.date,
            "entry_info": entry.info,
            "item_info": item_info,
        }

    def edit(self, index, new_info):
        """Изменить дополнительную информацию в записи"""
        if index < 0 or index >= len(self.__storage):
            return False

        entry = self.__storage[index]
        if entry is None:
            return False

        entry.info = new_info
        return True

    def classify(self, index):
        """Засекретить запись"""
        if 0 <= index < len(self.__storage) and self.__storage[index] is not None:
            self.__storage[index].classify()
            return True
        return False

    def declassify(self, index):
        """Рассекретить запись"""
        if 0 <= index < len(self.__storage) and self.__storage[index] is not None:
            self.__storage[index].declassify()
            return True
        return False

    def delete(self, index):
        """Удалить запись (заменить на None)"""
        if 0 <= index < len(self.__storage):
            self.__storage[index] = None
            return True
        return False

    @property
    def display(self):
        """Getter для отображения всего архива"""
        result = "=== АРХИВ КАЗНЫ ===\n"

        for i, entry in enumerate(self.__storage):
            result += f"[{i}] "
            if entry is None:
                result += "🗑️ УДАЛЕНО\n"
            else:
                result += str(entry) + "\n"
                if not entry.secret:
                    item = entry.item
                    if isinstance(item, Emerald):
                        statuses = ["Не учтён", "Учтён", "Под спудом"]
                        result += f"    Статус: {statuses[item.status]}, Цена: {item.price} золотых\n"
                    elif isinstance(item, Shell):
                        statuses = [
                            "Не учтена",
                            "Учтена",
                            "В отделении",
                            "Переплавлена",
                        ]
                        result += f"    Статус: {statuses[item.status]}, Цена: {item.price} золотых\n"
                    elif isinstance(item, Coin):
                        result += f"    Серия: {item.serial_number}, Год: {item.year}, Номинал: {item.value}\n"
                    if entry.info:
                        result += f"    Инфо: {entry.info}\n"
                else:
                    result += "    🔒 СЕКРЕТНО\n"
            result += "\n"

        return result

    def get_coins_info(self):
        """Получить информацию о всех монетах"""
        coins_info = []
        for i, entry in enumerate(self.__storage):
            if entry is not None and not entry.secret and isinstance(entry.item, Coin):
                coin = entry.item
                coins_info.append(
                    {
                        "index": i,
                        "serial_number": coin.serial_number,
                        "year": coin.year,
                        "value": coin.value,
                        "entry_info": entry.info,
                    }
                )
        return coins_info

    @property
    def _safe_storage_access(self):
        """Безопасный доступ к хранилищу для внутренних операций"""
        return self.__storage

    def get_entry(self, index):
        """Безопасное получение записи по индексу"""
        if 0 <= index < len(self.__storage):
            return self.__storage[index]
        return None


def main():
    # Создаем архив
    archive = Archive()

    print("=== ШАГ 1: Создание и учет 20 скорлупок и 10 изумрудов ===")
    shells = [Shell() for _ in range(20)]
    emeralds = [Emerald() for _ in range(10)]

    # Оцениваем и учитываем через безопасные методы
    for i, shell in enumerate(shells):
        shell.evaluate(50 + i)
        shell.account()
        archive.add(Entry(shell, info=f"Золотая скорлупка #{i+1}"))

    for i, emerald in enumerate(emeralds):
        emerald.evaluate(100 + i * 10)
        emerald.account()
        archive.add(Entry(emerald, info=f"Драгоценный изумруд #{i+1}"))

    print(archive.display)

    print("=== ШАГ 2: Отправка объектов ===")
    for i in range(len(archive._safe_storage_access)):
        entry = archive.get_entry(i)
        if entry:
            item = entry.item
            if isinstance(item, Emerald):
                item.store()
            elif isinstance(item, Shell):
                item.process()

    print(archive.display)

    print("=== ШАГ 3: Переплавка скорлупок в монеты ===")
    coin_counter = 1
    storage_size = len(archive._safe_storage_access)

    for i in range(storage_size):
        entry = archive.get_entry(i)
        if entry and isinstance(entry.item, Shell):
            shell = entry.item

            # Правильный порядок: создаем монету, потом меняем статус
            coin = Coin(f"CN-2024-{coin_counter:03d}", 2024, shell.price // 10)
            coin_entry = Entry(coin, info=f"Монета из скорлупки #{coin_counter}")
            archive.add(coin_entry)  # Сначала добавляем запись о монете

            shell.smelt()  # Потом меняем статус скорлупки
            coin_counter += 1

    print(archive.display)

    # ... остальные шаги с использованием безопасных методов ...

    print("=== ШАГ 4: Засекречивание изумрудов ===")
    # Засекречиваем все записи об изумрудах
    for i in range(len(archive._Archive__storage)):
        entry = archive._Archive__storage[i]
        if entry is not None and isinstance(entry.item, Emerald):
            archive.classify(i)

    print(archive.display)

    print("=== ШАГ 5: Удаление записей о скорлупках ===")
    # Удаляем записи о скорлупках
    for i in range(len(archive._Archive__storage)):
        entry = archive._Archive__storage[i]
        if entry is not None and isinstance(entry.item, Shell):
            archive.delete(i)

    print(archive.display)

    print("=== ШАГ 6: Рассекречивание части изумрудов ===")
    # Рассекречиваем каждую вторую запись об изумрудах
    for i in range(len(archive._Archive__storage)):
        entry = archive._Archive__storage[i]
        if entry is not None and isinstance(entry.item, Emerald) and i % 2 == 0:
            archive.declassify(i)
            archive.edit(i, "Рассекреченный изумруд высшего качества")

    print(archive.display)

    print("=== ШАГ 7: Информация о монетах ===")
    coins_info = archive.get_coins_info()
    print("Информация о всех монетах в архиве:")
    for coin in coins_info:
        print(
            f"Монета {coin['serial_number']}: номинал {coin['value']}, год {coin['year']}"
        )


if __name__ == "__main__":
    main()
