import string

s = 'Day, mice. "Year" is a mistake!'
result = ""
# 65 < x < 91 - eng капс
# 97 < x < 123 - eng строчные


def shift(str):
    """
    получает на ввод строку, разбивает и
    возвращает массив текстовых смещений (int)
    """
    shift_arr = []
    for word in str.split():
        shift_int = shift_arr.append(sum(1 for char in word if char.isalpha()))
    return shift_arr


for symb in s:
    if symb in string.ascii_letters:
        result += chr((ord(symb) + 3) % 26)
    else:
        result += symb

print(result)
