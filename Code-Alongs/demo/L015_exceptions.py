def input_int(prompt):
    while True:
        try:
            return int(input(f"input {prompt} "))
        except ValueError:
            print("my_iny is not an integer")       
            
age = input_int("age: ")
length = input_int("length: ")
weight = input_int("weight: ")
print(f"x = {age}, length = {length}, weight = {weight}")
