# 15.5 шифр цезаря
s = 'Блажен, кто верует, тепло ему на свете!'
# s = input()
result = ''
shift = -10
# 1040 < x < 1071 - русский капс
# 1072 < x < 1103 - руский строчные

for symb in s:
    if (1040 < ord(symb) < 1072) or (1072 < ord(symb) < 1103):
        result += chr(ord(symb)+shift)
    else:
        result += symb
print(result)