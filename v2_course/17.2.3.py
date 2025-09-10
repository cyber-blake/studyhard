import random

with open("lines.txt", "r", encoding="utf-8") as f:
    f = f.readlines()
    print(random.choice(f))
