# 15.5 шифр цезаря
import string
s = 'Day, mice. "Year" is a mistake!'
# shift of Day = 3 (no punct)
# сделать циклический сдвиг
# s = input()
result = ''
shift = 0


s_new = s.split()

for word in s_new:
    shift = word.count(string.ascii_letters)
    for symb in word:
        if symb in string.ascii_letters:
            result += chr(ord(symb)+shift)
        else:
            result += symb

print(result)
