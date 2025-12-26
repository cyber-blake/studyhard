def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            start = ord("a") if char.islower() else ord("A")
            # Вычисляем новую позицию с учетом сдвига и цикличности
            shifted_char_code = (ord(char) - start + shift) % 26 + start
            result += chr(shifted_char_code)
        else:
            result += char  # Не меняем символы, которые не являются буквами
    return result


# Пример использования
original_text = 'Day, mice. "Year" is a mistake!'
key = 3
encrypted_text = caesar_cipher(original_text, key)
print(f"Исходный текст: {original_text}")
print(f"Зашифрованный текст (сдвиг на {key}): {encrypted_text}")

# Для расшифровки достаточно применить ту же функцию с отрицательным сдвигом
decrypted_text = caesar_cipher(encrypted_text, -key)
print(f"Расшифрованный текст: {decrypted_text}")
