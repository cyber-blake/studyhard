import functools
import datetime
import inspect


def logging(log_file="function_calls.log"):
    """
    Декоратор для записи вызовов функции с аргументами в лог-файл.

    Args:
        log_file (str): Путь к файлу для записи логов. По умолчанию 'function_calls.log'
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Получаем текущее время
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Формируем строку с аргументами
            args_str = ", ".join([repr(arg) for arg in args])
            kwargs_str = ", ".join(
                [f"{key}={repr(value)}" for key, value in kwargs.items()]
            )
            all_args = ", ".join(filter(None, [args_str, kwargs_str]))

            # Получаем имя функции
            func_name = func.__name__

            # Формируем запись для лога
            log_entry = f"{timestamp} - {func_name}({all_args})"

            try:
                # Вызываем оригинальную функцию
                result = func(*args, **kwargs)

                # Добавляем результат в лог
                log_entry += f" -> {repr(result)}\n"

                # Записываем в файл
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(log_entry)

                return result

            except Exception as e:
                # Если произошла ошибка, записываем исключение
                log_entry += f" -> ERROR: {type(e).__name__}: {str(e)}\n"

                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(log_entry)

                # Пробрасываем исключение дальше
                raise

        return wrapper

    return decorator


# Альтернативная версия с дополнительной информацией
def logging_verbose(log_file="function_calls.log", include_module=True):
    """
    Расширенная версия декоратора логирования.

    Args:
        log_file (str): Путь к файлу для записи логов
        include_module (bool): Включать ли имя модуля в лог
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Формируем информацию о вызове
            module_info = f"{func.__module__}." if include_module else ""
            func_info = f"{module_info}{func.__name__}"

            # Получаем информацию о параметрах
            sig = inspect.signature(func)
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            args_str = ", ".join(
                [
                    f"{name}={repr(value)}"
                    for name, value in bound_args.arguments.items()
                ]
            )

            log_entry = f"{timestamp} - CALL: {func_info}({args_str})"

            try:
                result = func(*args, **kwargs)
                log_entry += f" -> RETURN: {repr(result)}\n"

                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(log_entry)

                return result

            except Exception as e:
                log_entry += f" -> EXCEPTION: {type(e).__name__}: {str(e)}\n"

                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(log_entry)

                raise

        return wrapper

    return decorator


# Пример использования
if __name__ == "__main__":
    # Простой пример
    @logging("example.log")
    def add_numbers(a, b):
        return a + b

    @logging("example.log")
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"

    @logging("example.log")
    def divide(a, b):
        return a / b

    # Тестируем функции
    print(add_numbers(5, 3))
    print(greet("Alice"))
    print(greet("Bob", greeting="Hi"))

    try:
        print(divide(10, 0))
    except:
        pass

    # Читаем и выводим содержимое лог-файла
    print("\nСодержимое лог-файла:")
    with open("example.log", "r", encoding="utf-8") as f:
        print(f.read())
