#Palindrome — Function + Return

def palindrome(text):
    text = text.lower()

    if text == text[::-1]:
        return True
    else:
        return False


word = input("Enter a word: ")

result = palindrome(word)

if result:
    print("Palindrome")
else:
    print("Not Palindrome")