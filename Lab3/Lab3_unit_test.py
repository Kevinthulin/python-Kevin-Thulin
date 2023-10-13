from Lab3_main import Shape

def Test_area():
    shape_instance = Shape(x=0, y=0)
    assert shape_instance.area == 0

    shape_instance = Shape(x=1, y=1)
    assert shape_instance.area == 1

