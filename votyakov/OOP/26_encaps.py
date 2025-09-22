from random import randint, random


class CRM:
    def __init__(self):
        self.__abiturients = {}

    def add(self, abiturient):
        number = abiturient.number  # получаем СНИЛС через свойство
        if number not in self.__abiturients:
            # добавление абитуриента в словарь под ключом СНИЛС
            self.__abiturients[number] = abiturient
        else:
            return "Такой студент уже есть в системе"

    def get_status(self, number):
        if number in self.__abiturients:
            abiturient = self.__abiturients[number]
            return abiturient._Abiturient__check()
        return "Абитуриент не найден в системе"


class Abiturient:
    def __init__(self, name, surname, patronymic, age, number, bvi=False):
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic
        self.__age = age
        # СНИЛС
        self.__number = number
        # Russian National Exam (ЕГЭ), баллы
        self.__RNE = self.__fetch_RNE()
        # есть ли БВИ
        self.__bvi = bvi
        # функция получения результатов ЕГЭ

    def __fetch_RNE(self):
        return tuple(randint(0, 100) for _ in range(3))
        # функция ответа на вопрос, проходит ли абитуриент

    def __check(self):
        if self.__bvi:
            return "Да"
        if random() > 0.95:
            return "Да"
        return "Нет"

    @property
    def number(self):
        return self.__number

    @property
    def FIO(self):
        return self.__surname, self.__name, self.__patronymic

    @FIO.setter
    def FIO(self, name, surname, patronymic):
        self.__name = name
        self.__surname = surname
        self.__patronymic = patronymic

    @property
    def RNE(self):
        return self.__RNE

    @RNE.setter
    def RNE(self, RNE):
        self.__RNE = RNE

    @property
    def bvi(self):
        return self.__bvi

    @bvi.setter
    def bvi(self, bvi):
        self.__bvi = bvi

    def __str__(self):
        return (
            f"Абитуриент: {self.FIO}, "
            f"Возраст: {self.__age}, "
            f"СНИЛС: {self.__number}, "
            f"Баллы ЕГЭ: {self.__RNE}, "
            f"БВИ: {'Да' if self.__bvi else 'Нет'}"
        )


module = CRM()

# добавление АР-а в список абитуриентов
module.add(Abiturient("Александр", "Вотяков", "Романович", 18, "111-222-333 00", True))
# добавление РА в список абитуриентов
module.add(Abiturient("Роман", "Вотяков", "Александрович", 18, "333-222-111 00"))
# проверка, проходят ли абитуриенты
print(module.get_status("111-222-333 00"))
print(module.get_status("333-222-111 00"))


# * 2
class Emerald:
    def __init__(self):
        # статус изумруда:
        # 0 - не учтён
        # 1 - учтён
        # 2 - отправлен под спуд
        self.__status = 0
        # цена изумруда
        self.__price = 0

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self): ...

    def account(self): ...

    def store(self): ...


class Shell:
    def __init__(self):
        # статус скорлупки:
        # 0 - не учтена
        # 1 - учтена
        # 2 - отправлена в монетолитейное отделение
        # 3 - переплавлена в монету
        self.__status = 0
        # цена скорлупки
        self.__price = 0


class Coin:
    def __init__(self, serial_number, year, value):
        # серийный номер монеты
        self.__serial_number = serial_number
        # год выпуска монеты
        self.__year = year
        # номинал монеты
        self.__value = value


### Запись (`Entry`)
class Entry:
    def __init__(self, item, date="01.01.1970", info="", secret=False):
        # идентификационный номер, создаётся автоматически
        self.__ID = self.__get_next_ID()
        # указатель на объект
        self.__item = item
        # дата создания записи
        self.__date = date
        # дополнительная информация об объекте
        self.__info = info
        # информация засекречена?
        self.__secret = secret

    def __get_next_ID(self):
        # можно создать свою функцию вместо этой
        return hash(self)


class Archive:
    def __init__(self):
        # список учтённых объектов
        self.__storage = []
