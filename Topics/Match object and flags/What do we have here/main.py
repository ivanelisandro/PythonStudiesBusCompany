import re

template = '... Jude'
string = input()
match = re.match(template, string)

if match:
    print(match.group())
else:
    print("None")
