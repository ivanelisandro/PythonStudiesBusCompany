import re

text = input()
template = "[a-zA-Z]+"
words = re.findall(template, text)
print(words)
