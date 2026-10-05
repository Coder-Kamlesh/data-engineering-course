#Pattern — Function + Argument

def pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()


number = int(input("Enter number of rows: "))

pattern(number)