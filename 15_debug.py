# * 1


def f(a):
    return 18 * a


print(f(1))

# ответ: 2. NameError: name ’b’ is not defined

# * 2
summa = 0
for i in range(1, 11):
    summa += i
print("The sum is:", summa)

# ответ 3. NameError: name 'summa' is not defined


# * 3
def is_even(n):
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")


is_even(4)

# ответ: 3 TypeError: not all arguments converted during string formatting


# * 4
def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(8))

# ответ: + заменен на  -
# * 5


def is_palindrome(s):
    s = s.lower()
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


print(is_palindrome("tenet"))


# * 6
def multiplylist(lst):
    if len(lst) == 0:
        return None
    else:
        result = 1
        for i in range(len(lst)):
            result = result * lst[i]
    return result
