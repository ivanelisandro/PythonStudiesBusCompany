import re       
names = input()
template = r"\d+"
print(re.split(template, names))
