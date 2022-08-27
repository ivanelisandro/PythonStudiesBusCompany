import re

string = input()
pattern = r"(?<=\$)\d+"
expenses = [int(cost) for cost in re.findall(pattern, string)]
total = sum(expenses)
print(f"This week you have spent: {total} dollars")
