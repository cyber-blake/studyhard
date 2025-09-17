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


Cam1 = PhotoCamera("Сanon", "077D", (1920, 1080), 2)
print(Cam1.get_camera_info())
print(Cam1.is_camera_on())
Cam1.turn_on()
Cam1.take_photo()
Cam1.take_photo()
Cam1.take_photo()
Cam1.store_photo()
Cam1.store_photo()
Cam1.view_photos()
Cam1.clear_memory()
Cam1.turn_off()
