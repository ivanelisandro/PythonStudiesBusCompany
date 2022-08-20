import re

template = 'are you ready??.?.?'

text = input()
match = re.match(template, text)

if match:
    print(match.end())
else:
    print(0)
