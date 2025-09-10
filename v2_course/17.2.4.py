with open("numbers.txt", "r", encoding="utf-8") as f:
    f = f.readlines()
    print(int(f[0]) + int(f[1]))
