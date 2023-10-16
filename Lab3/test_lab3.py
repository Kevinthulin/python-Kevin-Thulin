from Lab3_main import Shape, Sphere, Cube, Circle, Rectangle
import math

def test_Sphere():
    sphere1 = Sphere(0, 0, 0, 1)
    sphere2 = Sphere(0, 0, 0, 2)
    

    # Test volume
    assert math.isclose(sphere1.volume, 4/3 * math.pi, rel_tol=1e-9) # https://peps.python.org/pep-0485/
    assert math.isclose(sphere2.volume, 4/3 * math.pi * 8, rel_tol=1e-9) # https://peps.python.org/pep-0485/

    # Test equality and inequality
    assert sphere1 != sphere2
    assert not sphere1 == sphere2

    # Test ordering
    assert sphere1 < sphere2
    assert not sphere1 > sphere2

    # Test is_inside method
    assert sphere1.is_inside(0, 0, 0)
    assert not sphere1.is_inside(1, 1, 1)

    # Test translations
    sphere1.translate(1, 1, 1)
    assert sphere1.x == 1 and sphere1.y == 1 and sphere1.z == 1

    print("Sphere tests passed!")

def test_Cube():
    cube1 = Cube(0, 0, 0, 2)
    cube2 = Cube(0, 0, 0, 3)

    # Test volume
    assert cube1.volume == 8
    assert cube2.volume == 27

    # Test equality and inequality
    assert cube1 != cube2
    assert not cube1 == cube2

    # Test ordering
    assert cube1 < cube2
    assert not cube1 > cube2

    # Test is_inside method
    assert cube1.is_inside(0, 0, 0)
    assert not cube1.is_inside(2, 2, 2)

    print("Cube tests passed!")

def test_Circle():
    cir1 = Circle(0, 0, 1)
    cir2 = Circle(0, 0, 2)

    # Test area and circumference
    assert math.isclose(cir1.area, math.pi, rel_tol=1e-9) # https://peps.python.org/pep-0485/
    assert math.isclose(cir1.circumference, 2 * math.pi, rel_tol=1e-9) # https://peps.python.org/pep-0485/

    # Test equality and inequality
    assert cir1 != cir2
    assert not cir1 == cir2

    # Test ordering
    assert cir1 < cir2
    assert not cir1 > cir2

    # Test is_inside method
    assert cir1.is_inside(0, 0)
    assert not cir1.is_inside(2, 2)

    # Test translations
    cir1.translate(1, 1)
    assert cir1.x == 1 and cir1.y == 1

    print("Circle tests passed!")

def test_Rectangle():
    rectangle1 = Rectangle(0, 0, 2, 4)
    rectangle2 = Rectangle(0, 0, 3, 3)

    # Test area
    assert rectangle1.area == 8
    assert rectangle2.area == 9

    # Test equality and inequality
    assert rectangle1 != rectangle2
    assert not rectangle1 == rectangle2

    # Test ordering
    assert rectangle1 < rectangle2
    assert not rectangle1 > rectangle2

    # Test is_inside method
    assert rectangle1.is_inside(0, 0)
    assert not rectangle1.is_inside(2, 2)

    # Test translations
    rectangle1.translate(1, 1)
    assert rectangle1.x == 1 and rectangle1.y == 1

    print("Rectangle tests passed!")

def main():
    test_Sphere()
    test_Cube()
    test_Circle()
    test_Rectangle()
    print("All tests passed!")

if __name__ == "__main__":
    main()

