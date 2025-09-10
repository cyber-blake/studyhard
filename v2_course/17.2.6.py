with open(
    "prices.txt",
    "r",
    encoding="utf-8",
) as f:
    res_line = ""
    arr = []
    for line in f.readlines():
        res_line = line.split()
        arr.append(int(res_line[2]) * int(res_line[1]))
    print(sum(arr))
