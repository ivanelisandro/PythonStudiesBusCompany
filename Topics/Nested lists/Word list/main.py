text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]

length = int(input())
words = []

for line in text:
    for word in line:
        if len(word) <= length:
            words.append(word)

print(words)
