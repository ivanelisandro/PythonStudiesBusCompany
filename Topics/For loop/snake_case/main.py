variable = input()

result = ""
separator = "_"

for letter in variable:
    if letter.isupper():
        result += separator

    result += letter.lower()

print(result)
