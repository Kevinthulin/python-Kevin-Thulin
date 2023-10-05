import math


def main():
    for i in range(5):
        print(f"{i} = {square(i)}")

def square(n):
    return n * n

def greet(name = "World"):
    return f"Hello, {name}"


print(__name__)

if __name__ == "__main__":
    main()


