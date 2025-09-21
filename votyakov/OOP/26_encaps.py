from random import *


class CRM:
    def __init__(self):
        self.__abiturients = {}

    def add(self, abiturient):
        # получение СНИЛСа
        number = abiturient.get_number()
        # добавление абитуриента в словарь,
        # где информация хранится под СНИЛСами
        self.__abiturients[number] = abiturient

    def get_status(self): ...


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


module = CRM()

# добавление АР-а в список абитуриентов
module.add(Abiturient("Александр", "Вотяков", "Романович", 18, "111-222-333 00", True))
print(module.__dict__)
# добавление РА в список абитуриентов
module.add(Abiturient("Роман", "Вотяков", "Александрович", 18, "333-222-111 00"))
# проверка, проходят ли абитуриенты
print(module.get_status("111-222-333 00"))
print(module.get_status("333-222-111 00"))
