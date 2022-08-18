import re

name = input()
if re.match('[B-N][aeiou]', name):
    print("Suitable!")
