def print_case_counts(s):
    U = 0
    L = 0
    for symb in s:
        if symb.isupper():
            U += 1
        if symb.islower():
            L += 1

    print(f"Букв в верхнем регистре: {U}")
    print(f"Букв в нижнем регистре: {L}")


print_case_counts(input())
