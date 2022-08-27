import re

string = input()
pattern = r"(?<=<li>)[-\w\s]+(?=</li>)"
result = re.findall(pattern, string)

print(*result, sep="\n")
