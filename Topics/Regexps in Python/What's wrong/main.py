import re

text_1 = input()
text_2 = input()
if re.match(text_1, text_2):
    print(len(text_2) * 2)
else:
    print('no matching')
