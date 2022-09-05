import re


# put your regex in the variable template
template = "(Value|Name|Type)Error"
string = input()
result = re.match(template, string)
if result:
    print(result.group(1))
else:
    print("None")
