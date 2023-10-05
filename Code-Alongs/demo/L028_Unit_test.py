from L027_Module import square, greet

def main ():
    test_square()
# try:
#     assert 1 < 0
# except AssertionError:
#     print("1 is not less than zero")
def test_positive_square():
    assert square(2) == 4
    assert square(5) == 25
    
def test_negative_square():
    assert square(-2) == 4
    assert square(-5) == 25

def test_zero_square():
    assert square(0) == 0
    
def test_greet():
    assert greet() == "Hello, World"
    
def test_argument_greet():
    assert greet("Fredrik") == "Hello, Fredrik"




# print(L027_Module.square(9))

if __name__ == "__main__":
    main()