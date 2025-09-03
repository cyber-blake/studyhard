# * 15.5 шифр цезаря
"""
- проходим циклом по строке
- заменяем символ, если в аски_летерс + смещение
- смещение берем из нарезаного списка слов без пунктуации
"""
import string
s = 'Day, mice. "Year" is a mistake!'
# s = input()
def shift(str): 
    """
    возвращает массив текстовых смещений (int)
    """
    shift_arr = []
    for word in str.split():
        shift_int = shift_arr.append(sum(1 for char in word if char.isalpha()))
    return shift_arr


