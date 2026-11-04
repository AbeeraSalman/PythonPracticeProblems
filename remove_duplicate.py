text = input("Enter a word: ")
seen = set()
result = []

for ch in text:
    if ch not in seen:
        seen.add(ch)
        result.append(ch)

print("".join(result))