def selection_sort(arr):
    newArr = []
    temp = arr.copy()  # Работаем с копией

    for _ in range(len(temp)):
        min_val = min(temp)
        newArr.append(min_val)
        temp.remove(min_val)

    return newArr


arr = [10, 13, 4, 5, 6, 8]

print(selection_sort(arr))
