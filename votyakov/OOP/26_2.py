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
    def status(self, new_status=0):
        if new_status in (0, 1, 2) and new_status > self.__status:
            self.__status = new_status
            # * изменение статуса

    def account(self): ...

    def store(self): ...

    def estimate(self): ...

    @property
    def price(self):
        return self.__price

    def get_info(self):
        return (self.__status, self.__price)


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

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status=0):
        if new_status in (0, 1, 2) and new_status > self.__status:
            self.__status = new_status
            # * изменение статуса


class Coin:
    def __init__(self, serial_number, year, value):
        # серийный номер монеты
        self.__serial_number = serial_number
        # год выпуска монеты
        self.__year = year
        # номинал монеты
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
