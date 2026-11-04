
name = input("Enter your name: ").split()

short_word = name[0]

for word in name:
    if len(word) < len(short_word):
        short_word = word

print("Shortest word:", short_word)
