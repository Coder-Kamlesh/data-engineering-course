#Second Maximum Number
numbers = [10, 50, 30, 80, 40]

unique_numbers = list(set(numbers))

unique_numbers.sort()

print("Second maximum:", unique_numbers[-2])

# Yaha kya use hua?
# set()       # duplicates remove
# list()      # set ko list mein convert
# .sort()     # ascending sort
# [-2]        # second-last element