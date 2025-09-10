with open("nums.txt", "r", encoding="utf-8") as f:
    # f = f.read()
    # print(int(f[0].strip(" \t\n")) + int(f[1].strip(" \t\n")))
    x1 = [int(i) for i in f.read().split()]
    print(sum(x1))
