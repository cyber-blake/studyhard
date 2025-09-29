from abc import ABC, abstractmethod


class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        pass


class Autobiography(Book):
    def __init__(self, title, author) -> None:
        super().__init__(title, author)

    def display(self):
        print(
            f'"{self.title}" - прекрасная книга, написанная в автобиографическом жанре. Автор - {self.author}\n'
        )


class Psychology(Book):
    def __init__(self, title, author) -> None:
        super().__init__(title, author)

    def display(self):
        print(
            f'"{self.title}" - прекрасная книга, написанная в жанре психологии. Автор - {self.author}\n'
        )


class Fantasy(Book):
    def __init__(self, title, author) -> None:
        super().__init__(title, author)

    def display(self):
        print(
            f'"{self.title}" - прекрасная книга, написанная в жанре фентези. Автор - {self.author}\n'
        )


book1 = Autobiography("К черту все! Берись и делай!", "Ричард Брэнсон")
book2 = Psychology("Биология добра и зла", "Роберт Сапольски")
book3 = Fantasy("Песнь льда и пламени", "Джордж Реймонд Ричард Мартин")
book1.display()
book2.display()
book3.display()


# * 2
class Bird:
    def feed(self):
        print("Feeding bread crumbs")


class Swan(Bird):
    def feed(self):
        print("Feeding the swan bread crumbs")


class Duck(Bird):
    def feed(self):
        print("Feeding the duck bread crumbs")


class Mouse:
    def feed(self):
        print("Feeding the mouse bread crumbs")


def feed(bird: Bird):
    bird.feed()


feed(Duck())
feed(Mouse())
feed(Bird())
# answer: Некорректная аннотация типа - функция объявлена для Bird, но принимает Mouse


# * 3
class Human:

    def __init__(self, name: str):
        self.name = name

    def answer_question(self, question: str) -> str:
        return "Очень интересный вопрос! Давайте разбираться вместе!"


class Student(Human):

    def ask_question(self, human: Human, question: str):
        print(f"{human.name}, {question}")
        answer = human.answer_question(question)
        print(f"{answer}\n")


class Teacher(Human):

    def answer_question(self, question: str) -> str:
        question = question.lower()

        if "войти в айти" in question or "с чего начать" in question:
            return "Можешь начать осваивать программирование с ППШ"
        elif (
            "научиться программировать" in question
            or "изучить программирование" in question
        ):
            return "Сейчас расскажу"
        else:
            return super().answer_question(question)


class Mentor(Human):

    def answer_question(self, question: str) -> str:
        question = question.lower()

        if "эффективность" in question or "продуктивность" in question:
            return "Важно соблюдать три правила: планирование, фокус и отдых"
        elif "мотивация" in question or "не получается" in question:
            return "Главное - не сдаваться! Каждый программист через это проходит"
        else:
            return super().answer_question(question)


class Curator(Human):

    def answer_question(self, question: str) -> str:
        question = question.lower()

        if "додуматься" in question or "решение" in question or "алгоритм" in question:
            return "Сейчас опишу ход мыслей при решении задачи"
        elif "дедлайн" in question or "срок" in question:
            return "Давай составим план работы по этапам"
        else:
            return super().answer_question(question)


class CodeReviewer(Human):

    def answer_question(self, question: str) -> str:
        question = question.lower()

        if "проверить" in question or "ревью" in question or "код" in question:
            return "Проверил. Замечательный вариант решения. Вы отлично справились!"
        elif "ошибка" in question or "баг" in question:
            return "Проанализирую код и помогу найти проблему"
        else:
            return super().answer_question(question)


student1 = Student("Ваня")
teacher = Teacher("Александр Романович")
mentor1 = Mentor("Илья")
curator1 = Curator("Владимир")
reviewer1 = CodeReviewer("Евгений")

student1.ask_question(teacher, "как войти в айти?")
student1.ask_question(teacher, "как научиться программировать?")
student1.ask_question(mentor1, "как повысить эффективность работы?")
student1.ask_question(curator1, "как додуматься до этого решения?")
student1.ask_question(reviewer1, "я усовершенствовал свой код. Вы проверите?")


# * 4
class GeometricFigures:
    def __init__(self) -> None:
        pass

    def get_perimeter(self):
        pass

    def __str__(self) -> str:
        return "Периметр равен x"


#  ? ___________________________


class Triangle(GeometricFigures):

    def __init__(self, x, y, z) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f"Треугольник со сторонами {self.x}, {self.y}, {self.z}."

    def get_perimeter(self):
        return f"Периметр равен {self.x + self.y + self.z}"


class Rectangle(GeometricFigures):

    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Прямогуольник со сторонами {self.x}, {self.y}."

    def get_perimeter(self) -> str:
        return f"Периметр равен {(self.x + self.y)*2}"


class Square(GeometricFigures):

    def __init__(self, x) -> None:
        super().__init__()
        self.x = x

    def get_perimeter(self) -> str:
        return f"Периметр равен {self.x * 4}"

    def __str__(self) -> str:
        return f"Квадрат со стороной {self.x}."


figures = [
    Triangle(1, 2, 3),
    Triangle(4, 5, 6),
    Square(10),
    Square(20),
    Rectangle(6, 7),
    Rectangle(7, 8),
]

for figure in figures:
    print(figure, figure.get_perimeter())


# * 5


from abc import ABC, abstractmethod


class Command(ABC):
    """# - абстрактный класс `Command`, содержащий методы `vote_command()` и
    # `gesture_command()`;"""

    def __init__(self):
        pass

    @abstractmethod
    def vote_command(self):
        pass

    @abstractmethod
    def gesture_command(self):
        pass


class Lock(ABC):
    """
        # - дочерний класс `SmartAssistant`, который наследует абстрактные методы
    # класса `Command` и реализует собственные версии методов `vote_command()`
    # и `gesture_command()`;
    """

    @abstractmethod
    def close_lock(self):
        pass

    @abstractmethod
    def open_lock(self):
        pass


class SmartAssistant(Command):

    def __init__(self):
        super().__init__()

    def vote_command(self):
        print("Умный помощник распознал голосовую команду")

    def gesture_command(self):
        print("Умный помощник распознал жестовые команды")


class SmartCamera(Command, Lock):
    """
    # - дочерний класс `SmartCamera`, который наследует абстрактные методы двух
    # классов `Command` и `Lock` и реализует собственные версии методов
    # `close_lock()`, `open_lock()`, `vote_command()` и `gesture_command()`;
    """

    def __init__(self):
        super().__init__()

    def close_lock(self):
        print("Умная камера закрыла замок входной двери")

    def open_lock(self):
        print("Умная камера открыла замок входной двери")

    def vote_command(self):
        print("Умная камера распознала голосовую команду")

    def gesture_command(self):
        print("Умная камера распознала жестовые команды")


class SmartLock(Lock):
    """# - дочерний класс `SmartLock`, который наследует абстрактные методы класса
    # `Lock` и реализует собственные версии методов `close_lock()`,
    # `open_lock()
    """

    def close_lock(self):
        print("Умный замок закрыл входную дверь")

    def open_lock(self):
        print("Умный замок открыл входную дверь")


sa = SmartAssistant()
sa.vote_command()
sa.gesture_command()

sc = SmartCamera()
sc.open_lock()
sc.close_lock()
sc.vote_command()
sc.gesture_command()

sl = SmartLock()
sl.open_lock()
sl.close_lock()
