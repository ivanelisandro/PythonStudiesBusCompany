import re

string = input()
start = "<START>"
end = "<END>"
template = f"{start}(.+){end}"
result = re.search(template, string).group()
result = result.replace(start, "").replace(end, "")
print(result)
