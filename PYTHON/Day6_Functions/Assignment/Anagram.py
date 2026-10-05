#Anagram — Function + Arguments

def anagram(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()

    if sorted(text1) == sorted(text2):
        return True
    else:
        return False


word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

if anagram(word1, word2):
    print("Anagram")
else:
    print("Not Anagram")