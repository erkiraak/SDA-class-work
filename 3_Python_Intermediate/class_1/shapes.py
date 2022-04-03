from math import pi


class Shape:
    def __init__(self, name):
        self.name = name
        self.area_value = None
        self.circuit_value = None

    def __str__(self):
        return f"{self.name} - Area: {self.area_value}, circuit: {self.circuit_value}"


class Circle(Shape):
    def __init__(self, radius):
        Shape.__init__(self, __class__.__name__)
        self.radius = radius
        self.circuit_value = self.circuit()
        self.area_value = self.area()

    def circuit(self):
        return pi * self.radius

    def area(self):
        return pi * self.radius ** 2

class Square(Shape):
    def __init__(self, a):
        Shape.__init__(self, __class__.__name__)
        self.a = a
        self.circuit_value = self.circuit()
        self.area_value = self.area()

    def circuit(self):
        return self.a * 4

    def area(self):
        return self.a ** 2


class Triangle(Shape):
    def __init__(self, a, b, c, h):
        Shape.__init__(self, __class__.__name__)
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        self.circuit_value = self.circuit()
        self.area_value = self.area()

    def circuit(self):
        return self.a + self.b + self.c

    def area(self):
        return self.c * self.h * 0.5


class Parallelogram(Shape):
    def __init__(self, a, b, h):
        Shape.__init__(self, __class__.__name__)
        self.a = a
        self.b = b
        self.h = h
        self.circuit_value = self.circuit()
        self.area_value = self.area()

    def circuit(self):
        return (self.a + self.b) * 2

    def area(self):
        return self.b * self.h


class TriangleParallelogram(Triangle, Parallelogram):
    def __init__(self, a, b, c, h):
        Triangle.__init__(self, a, b, c, h)
        Parallelogram.__init__(self, a, b, h)
        Shape.__init__(self, __class__.__name__)
        self.circuit_value = self.circuit()
        self.area_value = self.area()

    def circuit(self):
        return Triangle.circuit(self) + Parallelogram.circuit(self)

    def area(self):
        return self.b * self.h * 2


triangle = Triangle(1, 2, 3, 2)
square = Square(2)
circle = Circle(3)
parallelogram = Parallelogram(2, 4, 3)
tp = TriangleParallelogram(2, 3, 4, 3.5)

print(triangle)
print(square)
print(circle)
print(parallelogram)
print(tp)
