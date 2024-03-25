import math

class Shape():
    def perimeter(self):
        return "I have no perimeter"
    
    def area(self):
        return "I have no area"
    
class Circle(Shape):
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        super().__init__()
        self.length = length
        self.width = width
    
    def perimeter(self):
        return 2 * self.length + 2 * self.width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, side1, side2, side3) -> None:
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
def main():
    shape = Shape()
    triangle = Triangle(3, 4, 5)
    circle = Circle(5)
    rectangle = Rectangle(5, 6)

    shape_list = [shape, triangle, circle, rectangle]

    for shape in shape_list:
        print("Perimeter: {}\n Area: {}\n".format(shape.perimeter(), shape.area()))

main()