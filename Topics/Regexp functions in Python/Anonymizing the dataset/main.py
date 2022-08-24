import re

string = input()
author = r"^@\w+"
others = r"@\w+"
result = re.sub(author, "<AUTHOR>", string)
result = re.sub(others, "<HANDLE>", result)
print(result)
