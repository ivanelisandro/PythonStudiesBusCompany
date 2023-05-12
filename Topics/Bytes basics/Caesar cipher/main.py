sentence = input()
new_letters = [chr(ord(letter) + 1) for letter in sentence]

print("".join(new_letters))
