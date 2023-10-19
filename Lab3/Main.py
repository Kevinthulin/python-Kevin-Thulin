from shapes2D import Circle, Rectangle
from shapes3D import Sphere, Cube

def main():
    
    circle1 = Circle(2, 3, 5)
    rect1 = Rectangle(2, 1, 10, 5)

    sphere1 = Sphere(4, 4, 4, 5)
    cube1 = Cube(1, 2, 3, 6.32)

    print(f"Circle details: {circle1}")
    print(f"Rectangle details: {rect1}")

    print(f"Sphere details: {sphere1}")
    print(f"Cube details: {cube1}")

if __name__ == '__main__':
    main()
