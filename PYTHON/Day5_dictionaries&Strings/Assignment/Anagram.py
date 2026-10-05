#Anagram

text1 = input("Enter first word: ")
text2 = input("Enter second word: ")

text1 = text1.lower()
text2 = text2.lower()

if sorted(text1) == sorted(text2):
    print("Anagram")
else:
    print("Not Anagram")