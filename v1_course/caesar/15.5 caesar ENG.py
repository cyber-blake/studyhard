# * 15.5 шифр цезаря
"""
- разбиваем по пробелу на слова
- проходим циклом по каждому слову, вложенным циклом по символу слова, заменяем на символы со сдвигом
- 
"""
import string
s = 'Day, mice. "Year" is a mistake!'
# s = input()
words = s.split() # * разбили по пробелl на слова с знаками препинания

for word in words: # цикл по словам 
    shift = sum(1 for char in word if char.isalpha())
    for symbol in word: # цикл по символам в слове
        if symbol in string.ascii_letters:
            result += chr(ord(symbol)+shift) # * доделать через джоин
            # ! нужно сохранить пунктуацию
        else:
            result += symbol
# ! сделать циклический сдвиг

print(result)
