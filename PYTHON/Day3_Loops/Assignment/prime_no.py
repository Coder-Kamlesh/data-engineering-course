num = int(input("Enter number: "))

count = 0

for i in range(2, num):
    if num % i == 0:
        count = count + 1

if count == 0:
    print("Prime")
else:
    print("Not Prime")