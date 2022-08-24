import re

user = input()
template = "[a-zA-Z]"

if re.match(template, user):
    print("Thank you!")
else:
    print("Oops! The username has to start with a letter.")
