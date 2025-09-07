# * 15.5 шифр цезаря
"""
- проходим циклом по строке
- заменяем символ, если в аски_летерс + смещение
- смещение берем из нарезаного списка слов без пунктуации
- добавляет в резалт
"""
s = input()
result = ""


def shift(str):
    """
    получает на ввод строку, разбивает и
    возвращает массив текстовых смещений (int)
    """
    shift_arr = []
    for word in str.split():
        shift_int = shift_arr.append(sum(1 for char in word if char.isalpha()))
        # список смещений пословно
    return shift_arr


my_iter = iter(shift(s))
words = s.split()
words_new = []
for word in words:
    shift = next(my_iter)
    new_word = ""
    for char in word:
        if char.isalpha():
            base = ord("a") if char.islower() else ord("A")
            new_word += chr((ord(char) - base + shift) % 26 + base)
        else:
            new_word += char
    words_new.append(new_word)


print(" ".join(words_new))
