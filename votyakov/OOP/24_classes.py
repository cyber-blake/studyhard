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
    def __init__(
        self,
        brand,
        model,
        resolution,
        memory_capacity,
    ):
        self.brand = brand
        self.model = model
        self.resolution = resolution
        self.memory_capacity = memory_capacity
        self.photos = {}
        self.is_on = False
        self.photo_count = 0

    def take_photo(self):
        import time

        if self.is_camera_on():
            print(
                f"Сделана фотография с разрешением {self.resolution[0]}x{self.resolution[1]} под именем Photo{self.photo_count:03d}"
            )
        else:
            print("как ты собрался фоткать на выключенную камеру?")

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
        import time

        self.photos[f"Photo{self.photo_count:03d}"] = (
            (self.resolution[0], self.resolution[1]),
            time.ctime(),
        )
        self.photo_count += 1

    def view_photos(self):
        for key, value in self.photos.items():
            print(f"{key}:{value}")

    def clear_memory(self):
        self.photos.clear()


# take_photo import pic_screenshot
canon = PhotoCamera("canon", "077D", (1920, 1080), 100)
print(canon.is_on)
print(canon.get_camera_info())
canon.turn_on()
canon.take_photo()
canon.store_photo()
canon.view_photos()
