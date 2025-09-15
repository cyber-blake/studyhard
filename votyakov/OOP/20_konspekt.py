class pas_student:
    def __init__(self, st_name, st_tariff, st_lessons):
        self.name = st_name
        self.__tariff = st_tariff
        self.__lessons = st_lessons

    def upgrade_tariff(self):
        if self.__tariff == "Стандарт":
            self.__tariff = "Pro"
        if self.__tariff == "База":
            self.__tariff = "Стандарт"

    def watch_lesson(self):
        self.__lessons += 1

    def show_lessons(self):
        return f"Количество просмотреных уроков = {self.__lessons}"

    def print_all(self):
        print(self.name, self.__lessons)


# s1 = pas_student("dima", "База", 20)
# print(s1.show_lessons())

# s1.watch_lesson()
# print(s1.show_lessons())
# s1.upgrade_tariff()
students = [
    pas_student("Петя", "Pro", 1),
    pas_student("Vanya", "Pro", 3),
    pas_student("Nikolay", "База", 5),
]

for st in students:
    st.print_all()


# * second podhod
students2 = [("Петя", "Pro"), ("Vanya", "Pro"), ("Nikolay", "База")]

list(map(print, students2))
