sentence = input("Enter a sentence: ")

words = sentence.split()

if words:
    largest_word = max(words, key=len)
    print("Largest word:", largest_word)
    print("Length:", len(largest_word))
else:
    print("The sentence is empty.")