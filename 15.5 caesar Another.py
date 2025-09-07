# * 15.5 шифр цезаря
"""
- разбиваем по пробелу на слова
- проходим циклом по каждому слову, вложенным циклом по символу слова, заменяем на символы со сдвигом
-
"""
import string

s = 'Day, mice. "Year" is a mistake!'
# s = input()
result = []
words = s.split()  # * разбил по пробелам на слова со знаками препинания

for word in words:  # цикл по словам
    new_word = ""
    shift = sum(1 for char in word if char.isalpha())
    for symbol in word:  # цикл по символам в слове
        if symbol in string.ascii_letters:
            new_symb = chr(ord(symbol) + shift)  # * доделать через джоин
            # ! нужно сохранить пунктуацию
            new_word += new_symb
    result.append(new_word)
# ! сделать циклический сдвиг

print(result)
