import re

string = input()
template = "^Good (morning|afternoon|evening)"
match = re.match(template, string)

if match:
    print(match.group())
else:
    print("No greeting!")
