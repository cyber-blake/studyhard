def bin_search(l: list, num: int):
    """
    Docstring for bin_search
    finding index of the given num in list l
    :param l: list of ints
    :type l: list
    :param num: number we are looking for
    :type num: int
    """
    l.sort()
    minimal = 0
    maximal = len(l) - 1
    # while len(l) > 1:
    #     mid = int((maximal + minimal) / 2)
    #     if num > l[mid]:
    #         # берем вторую часть списка
    #         minimal = mid
    #         maximal = len(l) - 1
    #     else:
    #         minimal = 0
    #         maximal = mid
    # return
    while minimal <= maximal:
        mid = minimal + maximal
        guess = l[mid]
        if guess == num:
            return mid
        elif guess > num:
            maximal = mid - 1
        else:
            minimal = mid + 1
    return


print(bin_search([0, 3, 4, 5, 8], 5))
