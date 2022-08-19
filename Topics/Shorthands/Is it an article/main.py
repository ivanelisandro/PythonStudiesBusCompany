import re

word = input()
template = r'the\b'
print(bool(re.match(template, word)))
