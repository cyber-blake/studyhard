def print_sorted_hyphen(s):
    List = s.split("-")
    List.sort()
    print("-".join(List))


print_sorted_hyphen(input())
