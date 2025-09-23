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

    def store(self):  # spood
        self.__status = 2

    # отправить под спуд (спрятать)

    def __str__(self) -> str:
        return f"{id(self)}, {self.__status}, {self.__price}"


class Shell:
    def __init__(self):
        # статус скорлупки:
        # 0 - не учтена
        # 1 - учтена - account()-ed
        # 2 - отправлена в монетолитейное отделение - process()-ed
        # 3 - переплавлена в монету - smelt()-ed
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

    def __str__(self) -> str:
        return f"{id(self)}, {self.__status}, {self.__price}"


class Coin:  # сделать серийный номер  random.choice(string.ascii_uppercase)

    def __init__(self, year, value):
        # год выпуска монеты
        self.__year = year
        # номинал монеты
        self.__value = value
        self.__serial_number = "TG" + str(id(self)) + "C"

    @property
    def serial_number(self):
        return self.__serial_number

    @property
    def year(self):
        return self.__year

    @property
    def value(self):
        return self.__value

    def __str__(self) -> str:
        return f"Serial: {self.__serial_number}, "


# class Entry:
#     _instance_count = 0

#     def __init__(self, item, date="01.01.1970", info="", secret=False):
#         # идентификационный номер, создаётся автоматически
#         self.__ID = self.__get_next_ID()
#         # указатель на объект
#         self.__item = item
#         # дата создания записи
#         self.__date = date
#         # дополнительная информация об объекте
#         self.__info = info
#         # информация засекречена?
#         self.__secret = secret
#         Entry._instance_count += 1

#     def __get_next_ID(self):
#         return id(self)

#     def __str__(self):
#         return f"Запись №{self._instance_count}: {self.__item}, year: {self.__date}, info:{self.__info} , is_secret: {self.__secret}"

from datetime import datetime


class Entry:
    _instance_count = 0
    _id_counter = 0

    def __init__(self, item, date="", info="", secret=False):
        Entry._instance_count += 1
        Entry._id_counter += 1

        # идентификационный номер, создаётся автоматически
        self.__ID = Entry._id_counter
        # указатель на объект
        self.__item = item
        # дата создания записи
        self.__date = date
        # дополнительная информация об объекте
        self.__info = info
        # информация засекречена?
        self.__secret = secret

        self.__date = (
            date if date else datetime.now().strftime("%d.%m.%Y %H:%M:%S.%f")[:-3]
        )
        self.__datetime_obj = datetime.now()

    def __get_next_ID(self):
        Entry._id_counter += 1
        return Entry._id_counter

    def __str__(self):
        return f"Запись №{self.__ID}: {self.__item}, дата: {self.__date}, инфо: {self.__info}, секретно: {self.__secret}"

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
        return self.__info if not self.__secret else "СЕКРЕТНО"

    @info.setter
    def info(self, new_info):
        self.__info = new_info

    @property
    def is_secret(self):
        return self.__secret

    # @classmethod
    # def get_total_entries(cls):
    #     return cls._instance_count


class Archive:
    def __init__(self):
        # список учтённых объектов
        self.__storage = []

    def add(self, new_entry):
        if isinstance(new_entry, Entry):
            self.__storage.append(new_entry)
        else:
            raise ValueError("Only Entries")

    def __str__(self) -> str: ...

    def classify(self):
        Entry.__secret = True

    def declassify(self):
        Entry.__secret = False


# * создайте архив;
# * создайте 20 объектов `Shell()` и 10 объектов `Emerald()`;
# * оцените все созданные объекты и учтите их в архиве, создав
# соответствующие записи `Entry()`;
# * отправьте все изумруды `Emerald()` под спуд, а скорлупки `Shell()` в
# монетолитейное отделение, обновив существующие записи о них;
# * переплавьте все золотые скорлупки `Shell()` в монеты `Coin()`, обновите
# существующие записи о скорлупках и создайте новые о монетах;
# * засекретьте все записи об изумрудах;
# * удалите записи о скорлупках;
# * рассекретьте часть записей об изумрудах;
# * добавьте дополнительную информацию к записям о рассекреченных
# изумрудах;
# * получите информацию о всех монетах в архиве

db = Archive()
l1 = []

for _ in range(20):
    l1.append(Shell())
for _ in range(10):
    l1.append(Emerald())

l2 = []
for x in l1:
    x.price = 200
    if isinstance(x, Emerald):
        x.store()
    l2.append(Entry(x))

print("Куча из 20 скорлупок и 10 изумрудов")
list(map(print, l1))
print("Набор записей обьектов")
list(map(print, l2))
