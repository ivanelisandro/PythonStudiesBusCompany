import re

string = input()
country_template = r"\+(\d{1})"
area_template = r"[-\s]?(\d{3})"
number_template = r"[-\s]?(\d{3}[-\s]?\d{2}[-\s]?\d{2})"
template = country_template + area_template + number_template

result = re.match(template, string)
if result:
    (country, area, number) = result.groups()
    print(f"Full number: {string}",
          f"Country code: {country}",
          f"Area code: {area}",
          f"Number: {number}",
          sep="\n")
else:
    print("No match")
