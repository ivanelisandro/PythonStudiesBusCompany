from lxml import etree


def find_in_elements(element):
    for member in element:
        password = member.get('password')
        if not password:
            password = find_in_elements(member)
        if password:
            return password
    return None


def find_password(xml_string):
    root = etree.fromstring(xml_string)
    return find_in_elements(root)
