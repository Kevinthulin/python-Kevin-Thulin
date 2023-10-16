import math

class Shape:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"(Shape centred at {self.y} and {self.x})"
    
    @staticmethod
    def validate_numeric_value(*args):
        """Validate that all arguments are numeric."""
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError (f"{arg} must be an int or floats")
            
    @staticmethod        
    def validate_positive_numbers(*nums):
        """Validate that all numbers are positive."""
        for num in nums:
            if not isinstance(num, (int, float)):
                raise ValueError(f"{num} must be a int or float")
            if num <= 0:
                raise ValueError(f"{num} must be a positive number")
    
    def same_metric_value(self, other):
        return isinstance(other, Shape)

class Shapes3D(Shape):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
        self.validate_numeric_value(x, y, z)
        
    def __eq__(self, other):
        if self.same_metric_value(other):
             return self.volume == other.volume
        return False
    
    def __lt__(self, other):
        if self.same_metric_value(other):
            return self.volume < other.volume
        return NotImplemented
    
    def __gt__(self, other):
        if self.same_metric_value(other):
            return self.volume > other.volume
        return NotImplemented
    
    def __le__(self, other):
        if self.same_metric_value(other):
            return self.volume <= other.volume
        return NotImplemented
    
    def __ge__(self, other):
        if self.same_metric_value(other):
            return self.volume >= other.volume
        return NotImplemented
    
    def translate(self, dx, dy, dz):
        self.validate_numeric_value(dx, dy, dz)
        self.x += dx
        self.y += dy
        self.z += dz
        
class Sphere(Shapes3D):
    def __init__(self, x, y, z, radius):
        super().__init__(x, y, z)
        self.radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self.validate_positive_numbers(value)
        self._radius = value
    
    @property
    def volume(self):
        return 4/3 * math.pi * (self.radius ** 3)
    
    def is_inside(self, px, py, pz):
        if (px - self.x) ** 2 + (py - self.y)** 2 + (pz - self.z)** 2 < self.radius ** 2:
            return True
        else:
            return False
    

class Cube(Shapes3D):
    def __init__(self, x, y, z, side_length):
        super().__init__(x, y, z)
        self.side_length = side_length
    
    @property
    def side_length(self):
        return self._side_length

    @side_length.setter
    def side_length(self, value):
        self.validate_positive_numbers(value)
        self._side_length = value
    
    @property 
    def volume(self):
        return self.side_length ** 3

    def is_inside(self, px, py, pz):
        if abs(self.x - px) < self.side_length/2 and abs(self.y - py) < self.side_length/2 and abs(self.z - pz) < self.side_length/2:
            return True
        else:
            return False
            
        
class Shapes2D(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.validate_numeric_value(x, y)
    
    def __eq__(self, other):
        if self.same_metric_value(other):
             return self.area == other.area
        return False
    
    def __lt__(self, other):
        if self.same_metric_value(other):
            return self.area < other.area
        return NotImplemented
    
    def __gt__(self, other):
        if self.same_metric_value(other):
            return self.area > other.area
        return NotImplemented
    
    def __le__(self, other):
        if self.same_metric_value(other):
            return self.area <= other.area
        return NotImplemented
    
    def __ge__(self, other):
        if self.same_metric_value(other):
            return self.area >= other.area
        return NotImplemented
    
    def translate(self, dx, dy):
        """Translate the shape by dx, dy along the x and y axis."""
        self.validate_numeric_value(dx, dy)
        self.x += dx
        self.y += dy

class Circle(Shapes2D):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self.validate_positive_numbers(value)
        self._radius = value

    @property
    def area(self):
        return math.pi * (self.radius ** 2)
    
    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self): 
        return f"Area of the circle is {self.area:.2f} and the circumference is {self.circumference:.2f} at postion x:{self.x} and y:{self.y}"
    
    def is_inside(self, px, py):
        """Check if a point is inside the circle."""
        if (px - self.x) ** 2 + (py - self.y)** 2 < self.radius ** 2:
            return True
        else:
            return False
        
    def __repr__(self):
        return (f"Circle: x = {self.x}, y = {self.y} and radius = {self.area}")
    
    def is_unit_cricle(self):
        if self.x == 0 and self.y == 0 and self.radius == 1:
            return "This is a unit cricle"
        return
    
class Rectangle(Shapes2D):
    def __init__(self, x, y, length, width):
        super().__init__(x, y)
        self.length = length
        self.width = width

    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        self.validate_positive_numbers(value)
        self._length = value

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self.validate_positive_numbers(value)
        self._width = value  

    @property
    def area(self):
        return self.width * self.length

    @property
    def circumference(self):
        return self.width + self.width + self.length + self.length
    
    def __str__(self):
        return f"Area of rectangle is {self.area:.2f} at postion x:{self.x} and y:{self.y}"
    
    def is_inside(self, px, py):
        """Check if a point is inside the rectangle."""
        if abs(self.x - px) < self.length/2 and abs(self.y - py) < self.width/2:
            return True
        else:
            return False
          
    def __repr__(self):
        return (f"Rectangle: x = {self.x}, y = {self.y}, Length: = {self.length} and width = {self.width}")

    def is_square(self):
        if self.length == self.width:
            return "This is square"
        



try:
    # Step 1: Create Instances
    circle1 = Circle(x=0, y=0, radius=4)
    circle2 = Circle(x=1, y=1, radius=3)
    rectangle = Rectangle(x=0, y=0, length=8, width=8)
    rectangle2 = Rectangle(x=0, y=0, length=4, width=4)
    
    # Step 2: Test __str__ Method
    print("String representations:")
    print(circle1)
    print(circle2)
    print(rectangle)
    print()
    
    # Step 3: Test area Property
    print("Areas:")
    print("Area of circle1:", circle1.area)
    print("Area of circle2:", circle2.area)
    print("Area of rectangle:", rectangle.area)
    print()
    
    # Step 4: Test Operator Overloading
    print("Operator Overloading:")
    print("Is circle1 == circle2?", circle1 == circle2)
    print("Is circle1 < rectangle?", circle1 > circle2)
    print("Is circle1 > rectangle?", rectangle2 < rectangle)
    print()
    
    # Step 5: Test translate Method
    print("Before translation, circle1 position:", circle1.x, circle1.y)
    circle1.translate(3, 3)
    print("After translation, circle1 position:", circle1.x, circle1.y)
    print()
    
    # Step 6: Test Error Handling
    print("Testing Error Handling:")
    try:
        circle1.translate("a", 3)
    except ValueError as e:
        print(f"Caught an error: {e}")
        # Step 7: Test is_inside Method for Circle
    print("Testing is_inside Method for Circle:")
    print("Is point (3, 3) inside circle1?", circle1.is_inside(4, 4))  # Should be True
    print("Is point (10, 10) inside circle1?", circle1.is_inside(10, 10))  # Should be False

    print("Testing is_inside Method for Sqaure:")
    print("Is point (3, 3) inside Square1?", rectangle.is_inside(1, 2))  # Should be True
    print("Is point (10, 10) inside square1?", rectangle.is_inside(10, 10))  # Should be False

except Exception as e:
    print(f"An unexpected error occurred: {e}")

