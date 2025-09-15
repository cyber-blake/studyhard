def deliteli(n):
    return False if [x for x in range(2, n) if n % x == 0] else True


# ? все делители числа кроме 1 и самого числа n

# for x in range(2, 11):  # простые числа - True  (2,3,4,5,6,7,8,9,10)
#     print(deliteli(x))


print(deliteli(7))
print(deliteli(19))
