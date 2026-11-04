
sentence = input("Enter a sentence: ").split()

longest_word = sentence[0]

for word in sentence:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)
