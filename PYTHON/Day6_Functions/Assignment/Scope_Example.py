#Scope Example

x = 100          # Global variable


def test():
    y = 50       # Local variable

    print("Inside function:", x)
    print("Inside function:", y)


test()

print("Outside function:", x)