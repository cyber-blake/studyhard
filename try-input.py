while True:
    try:
        user_summ = float(input("Введите сумму, которую хотите конвертировать: "))
        break  # Если успешно, выходим из цикла
    except ValueError:
        print("Ошибка! Введите сумму цифрами (например: 100 или 50.5)")

print(f"Вы ввели: {user_summ}")

