import math

class Shape:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"(Shape centred at {self.y} and {self.x})"
    
    def __eq__(self, other):
        if isinstance(other, Shape):
            return self.area == other.area
        return False
    
    def __lt__(self, other):
        if isinstance(other, Shape):
            return self.area < other.area
        return True
    def __gt__(self, other):
        if isinstance(other, Shape):
            return self.area > other.area
        return True
    def __le__(self, other):
        if isinstance(other, Shape):
            return self.area <= other.area
        return True
    def __ge__(self, other):
        if isinstance(other, Shape):
            return self.area >= other.area
        return True
    def translate(self, dx, dy):
        if not (isinstance(dx, (int, float)) and isinstance(dy, (int, float))):
            raise ValueError("dx and dy must be numbers")
        self.x += dx
        self.y += dy

    def is_inside(self, px, py):
        if not (isinstance(px, (int, float)) and isinstance(py, (int, float))):
            raise ValueError("px and py must be numbers")

class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    
    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Area of the circle is {self.radius} at postion x:{self.x} and y:{self.y}"
    
class Rectangle(Shape):
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.width * self.length
    
    def __str__(self):
        return f"Area of rectangle is {self.area} at postion x:{self.x} and y:{self.y}"
    

 