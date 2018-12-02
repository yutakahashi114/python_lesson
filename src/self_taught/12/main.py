import math

class Orange:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color
        self.mold = 0
        print("created!")
    def rot(self, days, temp):
        """ temp : 摂氏"""
        self.mold = days * temp

orange1 = Orange(10, "dark orange")
print(orange1.weight)
print(orange1.color)

orange1.weight = 100
orange1.color = "light orange"

print(orange1.weight)
print(orange1.color)

orange2 = Orange(4, "dark orange")
orange3 = Orange(8, "yellow")

orange1.rot(10, 37)
print(orange1.mold)

class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def change_size(self, width, length):
        self.width = width
        self.length = length

rectangle = Rectangle(10, 20)
print(rectangle.area())
rectangle.change_size(20, 40)
print(rectangle.area())

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

circle = Circle(4)
print(circle.area())

class Triangle:
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height / 2

class Hexagon:
    def __init__(self, side):
        self.side = side
    def calculate_perimeter(self):
        return self.side * 6

class Shape:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def print_size(self):
        print("{} by {}".format(self.width, self.length))

class Square(Shape):
    def area(self):
        return self.width * self.length
    def print_size(self):
        print("I am {} by {}".format(self.width, self.length))

a_square = Square(20, 20)
a_square.print_size()
print(a_square.area())

class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick")
stan = Dog("Stan", "Bulldog", mick)
print(stan.owner.name)
