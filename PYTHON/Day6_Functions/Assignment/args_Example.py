#*args Example

def add_numbers(*args):
    total = 0

    for number in args:
        total = total + number

    return total


result = add_numbers(10, 20, 30, 40)

print("Total:", result)