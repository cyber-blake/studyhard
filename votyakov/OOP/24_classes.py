class CoffeeMachine:
    """
    сыпучие продукты в граммах, жидкие - в милилитрах
    """

    def __init__(self, water_level, coffee_level, milk_level, sugar_level=0, cups=0):
        self.water_level = water_level
        self.coffee_level = coffee_level
        self.milk_level = milk_level
        self.sugar_level = sugar_level
        self.cups = cups

    def add_water(self, amount):
        self.water_level += amount

    def add_coffee(self, amount):
        self.coffee_level += amount

    def add_milk(self, amount):
        self.milk_level += amount

    def add_sugar(self, amount):
        self.sugar_level += amount

    def add_cups(self, amount):
        self.cups += amount

    def show_resources(self):
        print(
            [
                self.coffee_level,
                self.water_level,
                self.milk_level,
                self.sugar_level,
                self.cups,
            ]
        )

    def check_resources(self):
        return all(
            [
                self.coffee_level > 18,
                self.water_level > 50,
                self.milk_level > 120,
                self.sugar_level > 10,
                self.cups > 0,
            ]
        )

    def make_coffee(self):
        if self.check_resources():
            self.coffee_level -= 18
            self.water_level -= 50
            self.milk_level -= 120
            self.sugar_level -= 10
            self.cups -= 1
            print("Кофе готов!")
        else:
            print("Недостаточно ингридиентов! :(")


# braun = CoffeeMachine(200, 10, 50)
# braun.show_resources()
# braun.add_coffee(20)
# braun.add_cups(10)
# braun.add_sugar(100)
# braun.add_milk(500)
# braun.show_resources()
# braun.make_coffee()
# braun.make_coffee()


# * 2
# ?_____________________________________________________________


class PhotoCamera:
    def __init__(self, brand, model, resolution=(1920, 1080), memory_capacity=10):
        self.brand = brand
        self.model = model
        self.resolution = resolution
        self.memory_capacity = memory_capacity
        self.is_on = False
        self.photo_count = 0
        self.photos = {}

    def take_photo(self):
        import time

        if self.is_camera_on():
            print(
                f"Сделана фотография с разрешением {self.resolution[0]}x{self.resolution[1]} под именем Photo{self.photo_count:03d}"
            )
            self.store_photo()
        else:
            print("Как ты собрался фоткать на выключенную камеру?")

    def get_camera_info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Разрешение: {self.resolution[0]}x{self.resolution[1]}"

    def turn_on(self):
        self.is_on = True
        print("Фотокамера включена")

    def turn_off(self):
        self.is_on = False
        print("Фотокамера выключена")

    def is_camera_on(self):
        return self.is_on

    def store_photo(self):
        if len(self.photos) < self.memory_capacity:
            import time

            current_time = time.ctime()
            photo_name = f"Photo{self.photo_count:03d}"
            self.photos[photo_name] = (
                (self.resolution[0], self.resolution[1]),
                current_time,
            )
            print(f"Фото {photo_name} успешно сохранено")
            self.photo_count += 1  # Увеличиваем после сохранения
        else:
            print("Память переполнена. Удалите фотографии")

    def view_photos(self):
        if not self.photos:
            print("Нет сохраненных фотографий")
            return

        print("\n=== СОХРАНЕННЫЕ ФОТОГРАФИИ ===")
        for key, value in self.photos.items():
            print(f"{key}, разрешение: {value[0][0]}x{value[0][1]}, время: {value[1]}")
        print(f"Всего фотографий: {len(self.photos)}/{self.memory_capacity}")

    def clear_memory(self):
        self.photos.clear()
        self.photo_count = 0
        print("Фото удалены")


# Cam1 = PhotoCamera("Сanon", "077D", (1920, 1080), 2)
# print(Cam1.get_camera_info())
# print(Cam1.is_camera_on())
# Cam1.turn_on()
# Cam1.take_photo()
# Cam1.take_photo()
# Cam1.take_photo()
# Cam1.store_photo()
# Cam1.store_photo()
# Cam1.view_photos()
# Cam1.clear_memory()
# Cam1.turn_off()

# ?_____________________________________________________________


# * 3
class Revolver:
    def __init__(self):
        from itertools import cycle

        self.MAX_CAPACITY = 6
        non_tuple = list(range(1, 7))
        self.slots = dict.fromkeys(non_tuple, None)  # словарь 1: None, 2: None, etc
        self.slots_cycle = cycle(self.slots)
        self.slot_pointer = 1
        print(type(self.slots))
        print(type(self.slots_cycle))
        print(type(self.slot_pointer))

    def show_baraban(self):
        print(self.slots)

    def add_bullet(self, bullet):
        self.slots[self.slot_pointer] = bullet

    def add_bullets_from_list(self, list):
        if len(list) <= self.MAX_CAPACITY:
            ...

    def shoot(self):
        if self.slot_pointer != None:
            print("BANG!!!")
            next(self.slots_cycle)
        else:
            return None

    # def unload(self, all_items=False):

    def scroll(self):
        import random

        self.slot_pointer = random.randint(1, 6)
        print("Крутите барабан! Буква А! (барабан покручен)")
        print(self.slot_pointer)

    # def bullet_count(self):


# * play russian roulette


r1 = Revolver()
r1.show_baraban()
r1.scroll()
