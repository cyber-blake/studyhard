import sys
import importlib


def imp_modules(mods):

    caller_globals = sys._getframe(1).f_globals

    for module_name in mods:
        try:
            module = importlib.import_module(module_name)

            caller_globals[module_name] = module

            print(f"Модуль {module_name} успешно импортирован")
        except Exception as e:
            print(f" Непредвиденная ошибка с модулем {module_name}: {e}")
