#Factorial

def calculate_factorial(number):

    result = 1

    for i in range(1, number + 1):
        result = result * i

    return result


number = int(input("Enter a number: "))

answer = calculate_factorial(number)

print("Factorial:", answer)