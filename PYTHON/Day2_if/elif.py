marks = int(input("Enter Marks :"))
if (marks >= 90):
    print("Your grade Is A+.")
elif (marks >= 75 and marks <= 89):
        print("Your grade Is A")
elif (marks >= 60 and marks <= 74):
        print("Your grade Is B")
elif (marks >= 35 and marks <= 59):
        print("Your grade Is C")
elif (marks < 89):
        print("Your Are Fail")
else:
    print("You Are Enter Wrong")