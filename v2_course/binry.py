def view_binary_file(filename):
    with open(filename, "rb") as file:
        content = file.read()
        print(f"Размер файла: {len(content)} байт")
        print("Двоичное представление:")
        for i, byte in enumerate(content):
            print(f"{byte:08b}", end=" ")
            if (i + 1) % 8 == 0:
                print()
        print("\n\nШестнадцатеричное представление:")
        for i, byte in enumerate(content):
            print(f"{byte:02X}", end=" ")
            if (i + 1) % 16 == 0:
                print()


# Использование
print(view_binary_file("prices.txt"))


def detailed_binary_view(filename):
    with open(filename, "rb") as file:
        content = file.read()

        print("Offset(h) 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F  ASCII")
        print("-" * 60)

        for i in range(0, len(content), 16):
            chunk = content[i : i + 16]

            # HEX представление
            hex_part = " ".join(f"{b:02X}" for b in chunk)

            # ASCII представление
            ascii_part = "".join(chr(b) if 32 <= b <= 126 else "." for b in chunk)

            print(f"{i:08X}  {hex_part:<47}  {ascii_part}")


# Использование
print(detailed_binary_view("prices.txt"))
