#tudent marks processor:

marks = [75, 88, 92, 67, 85, 90]

# Average
total = sum(marks)
average = total / len(marks)

print("Average marks:", average)

# Topper
topper = max(marks)

print("Topper marks:", topper)

# Ascending sorting
marks.sort()

print("Marks in ascending order:", marks)

# Descending sorting
marks.sort(reverse=True)

print("Marks in descending order:", marks)