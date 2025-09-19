#
# * 1
class SignedMessage:
    """
    `message` - сообщение, представленное строкой, а
    `signature`- очень крутая подпись
    """

    def __init__(self, message, signature) -> None:
        self.message = message
        self.signature = signature

    def __str__(self) -> str:
        return f"{self.message} {self.signature}"

    def __add__(self, other) -> str:
        return f"{self.message} {other}"


SIGNATURE = "-~=$([{PETR}])$=~-"

# выводится "Hello -~=$([{PETR}])$=~-"
print(SignedMessage("Hello ", SIGNATURE))

# выводится "world! -~=$([{PETR}])$=~-"
print(SignedMessage("world!", SIGNATURE))

# выводится "Hello world! -~=$([{PETR}])$=~-"
print(SignedMessage("Hello ", SIGNATURE) + SignedMessage("world!", SIGNATURE))
# * 2


class Vector2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


class Vector3:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y, self.z - other.z)

    def __neg__(self):
        return (-self.x, -self.y, -self.z)

    def __abs__(self):
        import math

        x = self.x**2 + self.y**2 + self.z**2
        return int(math.sqrt(x))

    def __str__(self) -> str:
        t = {self.x, self.y, self.z}
        return f"{t}"


a = Vector3(1, -2, 3)
b = Vector3(3, 4, 5)
print(a - b)
print(a + b)
c = Vector3(1, 0, -1)
print(-c)
d = Vector3(3, 4, 0)
print(abs(d))
print(d)
