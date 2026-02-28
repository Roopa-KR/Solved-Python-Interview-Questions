# Parent Class
from abc import ABC , abstractmethod
class Shape:
    @abstractmethod
    def __init__(self):
        print("Area Calculation Started")


# Child Class 1
class Rectangle(Shape):
    @abstractmethod
    def __init__(self, l, b):
        super().__init__()   # calling parent constructor
        self.length = l
        self.breadth = b

    def area(self):
        
        print("Rectangle Area =", self.length * self.breadth)


# Child Class 2
class Circle(Shape):
    @abstractmethod
    def __init__(self, r):
        super().__init__()   # calling parent constructor
        self.radius = r

    def area(self):
        print("Circle Area =", 3.14 * self.radius * self.radius)


# Object Creation
r = Rectangle(4, 5)
c = Circle(3)

r.area()
c.area()