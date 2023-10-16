from Lab3_main import Shape, Sphere, Cube, Circle, Rectangle
import math

# Initialize Shape objects
shape1 = Shape(2, 3)
shape2 = Shape(5, 5)

# Test Shape attributes
assert shape1.x == 2
assert shape1.y == 3

# Test Sphere objects
sphere1 = Sphere(0, 0, 0, 1)
sphere2 = Sphere(0, 0, 0, 2)

# Test Sphere volume
assert math.isclose(sphere1.volume, 4/3 * math.pi, rel_tol=1e-9)
assert math.isclose(sphere2.volume, 4/3 * math.pi * 8, rel_tol=1e-9)

# Test Sphere equality
assert not sphere1 == sphere2

# Test Sphere ordering
assert sphere1 < sphere2
assert not sphere1 > sphere2

# Test Cube objects
cube1 = Cube(0, 0, 0, 2)
cube2 = Cube(0, 0, 0, 3)

# Test Cube volume
assert cube1.volume == 8
assert cube2.volume == 27

# Test Cube equality
assert not cube1 == cube2

# Test Cube ordering
assert cube1 < cube2
assert not cube1 > cube2

# Initialize Circle objects
circle1 = Circle(0, 0, 1)
circle2 = Circle(0, 0, 2)

# Test Circle area and circumference
assert math.isclose(circle1.area, math.pi, rel_tol=1e-9)
assert math.isclose(circle1.circumference, 2 * math.pi, rel_tol=1e-9)

# Test Circle equality and ordering
assert not circle1 == circle2
assert circle1 < circle2
assert not circle1 > circle2

# Initialize Rectangle objects
rectangle1 = Rectangle(0, 0, 2, 4)
rectangle2 = Rectangle(0, 0, 3, 3)

# Test Rectangle area
assert rectangle1.area == 8
assert rectangle2.area == 9

# Test Rectangle equality and ordering
assert not rectangle1 == rectangle2
assert rectangle1 < rectangle2
assert not rectangle1 > rectangle2

# Test translations

sphere1.translate(1, 1, 1)
assert sphere1.x == 1
assert sphere1.y == 1
assert sphere1.z == 1

circle1.translate(1, 1)
assert circle1.x == 1
assert circle1.y == 1

rectangle1.translate(1, 1)
assert rectangle1.x == 1
assert rectangle1.y == 1

print("All tests passed!")