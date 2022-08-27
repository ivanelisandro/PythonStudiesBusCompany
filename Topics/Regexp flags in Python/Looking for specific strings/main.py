import re

string = input()
pattern = "^b.*l$"
result = re.search(pattern, string, re.DOTALL | re.IGNORECASE)

if result:
    print(result.group())
else:
    print("No match")
