#Prime Number

def check_prime(number):

    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

result = check_prime(number)

if result:
    print("Prime Number")
else:
    print("Not Prime Number")