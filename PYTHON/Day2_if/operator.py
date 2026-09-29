year = int(input("Enter Year : "))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} This is  Leap Year.")
else:
    print(f"{year} this is Not Leap Year.")
