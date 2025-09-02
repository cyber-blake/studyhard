s = 'Day, mice.'
result = ''
shift = 3
for symb in s:
    result += chr(ord(symb)+shift)
print(result)