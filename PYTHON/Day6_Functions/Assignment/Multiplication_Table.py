#Multiplication Table

def multiplication_table(number):

    for i in range(1, 11):
        print(number, "x", i, "=", number * i)


number = int(input("Enter a number: "))

multiplication_table(number)