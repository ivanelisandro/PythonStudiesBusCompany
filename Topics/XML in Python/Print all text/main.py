from lxml import etree


root = etree.fromstring(input())
print(*[element.text for element in root], sep='\n')
