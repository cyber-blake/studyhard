# 15.5 шифр цезаря
import string
s = 'Day, mice. "Year" is a mistake!'
# s = input()
result = []
words = s.split() # разбили по пробелу на слова с знаками препинания

for word in words:
    shift = sum(1 for char in word if char.isalpha())
    new_word = ''
    for symb in word:
        if symb in string.ascii_letters:
            new_symb = chr(ord(symb)+shift) # доделать через джоин
            new_word += new_symb
        result.append(new_word)
# сделать циклический сдвиг

print(result)
