class Emerald:
    def __init__(self):
        # статус изумруда:
        # 0 - не учтён
        # 1 - учтён
        # 2 - отправлен под спуд
        self.__status = 0
        # цена изумруда
        self.__price = 0

    @property  # getter
    def status(self):
        print("getter worked")
        return self.__status

    @status.setter
    def status(self, new_status):
        if new_status in (0, 1, 2) and new_status >= self.__status:
            self.__status = new_status
            # * изменение статуса

    @property  # getter
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def account(self): ...

    # ?????????? сделать запись в базе данных (как делать базу???)

    def store(self):
        self.__status = 2

    # отправить под спуд (спрятать)


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

    @property  # getter
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        if new_status in (0, 1, 2, 3) and new_status > self.__status:
            self.__status = new_status
            # * изменение статуса

    # вызывать сеттер внутри класса шелл

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    # внести в базу данных
    def account(self): ...

    def process(self):
        self.__status = 2

    def smelt(self):
        self.__status = 3
        # создать обьект Coin()


class Coin:  # подумать, как сделать серийный номер (присваивать по порядку, перемешивая цифры и буквы) HJK-###-980-AE374K, random.choice(string.ascii_uppercase)

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
    def __init__(
        self, item, date="01.01.1970", info="", secret=False
    ):  # можно поработать с модулем дата
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


em1 = Emerald
print(em1)
em1.status = 2
em1.price = 1000
print(em1.price)
