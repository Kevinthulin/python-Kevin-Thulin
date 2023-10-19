from Shape import Shape
import math

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
   
    def __str__(self):
        return f"This sphere has a radius of: {self.radius:.2f} and volume of: {self.volume:.2f} at postion x: {self.x}, y:{self.y}, z: {self.z}"

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
    
    def __str__(self):
        return f"This Cube has length of it sides: {self.side_length:.2f} and volume of: {self. volume:.2f} at postion x: {self.x}, y:{self.y}, z: {self.z}"
    
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
        