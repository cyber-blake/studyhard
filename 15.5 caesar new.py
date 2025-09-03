# * 15.5 шифр цезаря
"""
- проходим циклом по строке
- заменяем символ, если в аски_летерс + смещение
- смещение берем из нарезаного списка слов без пунктуации
- добавляет в резалт
"""
import string
s = 'Day, mice. "Year" is a mistake!'
# s = input()
result = ''
def shift(str): 
    """
    получает на ввод строку, разбивает и
    возвращает массив текстовых смещений (int)
    """
    shift_arr = []
    for word in str.split():
        shift_int = shift_arr.append(sum(1 for char in word if char.isalpha()))
    return shift_arr

my_iter = iter(shift(s))

for word in s.split(): 
#  проблема в том, что разбивает на слова через пробел, иначе не сможет для каждого слова получать смещение

    shift = next(my_iter)
    for symb in word:
        if symb in string.ascii_letters:
            result += chr(ord(symb)+shift)
        else:
            result += symb
        
print(result)
