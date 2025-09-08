# * №1
names = ["Александр", "Алекс", "Альберт"]
surnames = ["Вотяк", "Вотяков", "Вотякович"]
paternal = ["Романович"]

# for x in names:
#     for y in surnames:
#         print(f"Диплом с отличием вручается {y}y {x}y {paternal[0]}у")

# # * №2
# A = input()
# B, C = int(input()), int(input())

# print(f"{A}{B:04}-{C:03}")


# # * №3
# first = int(input())
# second = int(input())
# print(f"{first:>9}")
# print(f"{second:>9}")
# print(f"{first+second:>9}")

# # * №4
# r = int(input()) / 10  # rate
# k = int(input())
# summ = 100_000_000
# res = summ * ((1 + r / 12) ** k)
# print(f"{res:,.2f}")


# # * №5

# for a in range(1, 11):  # Внешний цикл для множителя (числа от 1 до 10)
#     for b in range(1, 11):  # Внутренний цикл для множителя (числа от 1 до 10)
#         product = a * b
#         if "0" in str(product):
#             print(f"[DEBUG] {a=} {b=} {product=}")

# # * 6
a, b, c, d = map(int, input().split())

temp_bin_byte = f"{a:08b}.{b:08b}.{c:08b}.{d:08b}"
temp_bin = f"{a:>29b}.{b:b}.{c:b}.{d:b}"
temp_oct = f"{a:>29o}.{b:o}.{c:o}.{d:o}"
temp_dec = f"{a:>29d}.{b:d}.{c:d}.{d:d}"
temp_hex = f"{a:>29x}.{b:x}.{c:x}.{d:x}"

if not all(0 <= x < 256 for x in [a, b, c, d]):
    print("Число вне диапазона")
else:
    print(temp_bin_byte.format(a, b, c, d))
    print(temp_bin.format(a, b, c, d))
    print(temp_oct.format(a, b, c, d))
    print(temp_dec.format(a, b, c, d))
    print(temp_hex.format(a, b, c, d))
