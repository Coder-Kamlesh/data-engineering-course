#Word Frequency — Function + Dictionary

def word_frequency(text):
    words = text.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


sentence = input("Enter a sentence: ")

result = word_frequency(sentence)

print("Word Frequency:", result)