class Rectangle:
    recs = []

    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.recs.append((self.width, self.length))

    def print_size(self):
        print("{0} by {1}".format(self.width, self.length))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)

class Lion:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

lion = Lion("Dilbert")
print(lion)

class AlwaysPositive:
    def __init__(self, number):
        self.n = number
    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x+y)
