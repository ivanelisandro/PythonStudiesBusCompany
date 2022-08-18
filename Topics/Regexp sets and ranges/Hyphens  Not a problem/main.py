import re

# your code here
word = input()
template = '.{1,}-.{1,}'

print(bool(re.match(template, word)))
