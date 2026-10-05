#Fibonacci

def fibonacci(terms):

    a = 0
    b = 1

    for i in range(terms):
        print(a, end=" ")

        next_number = a + b
        a = b
        b = next_number


number = int(input("Enter number of terms: "))

fibonacci(number)