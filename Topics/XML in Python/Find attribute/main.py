from lxml import etree


root = etree.fromstring(input())
attribute = input()

print(root.get(attribute))
