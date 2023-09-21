# scope, life-time of a variable.
# local scope: only avaliable locally in a function
# global scope: avaliable through execution of program
name = "Kevin"

def main():
    print(name)

print(name)
main()


# python dosen't have block scope, but this is used in most other langugaes, suck as c#, C, C++.
# for i in range(10):
#     print(i)

# print(f"i = {i}")

