

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