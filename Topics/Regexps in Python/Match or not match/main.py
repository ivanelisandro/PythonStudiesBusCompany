import re


def matched(template, string):
    pattern = re.compile(template)
    return bool(pattern.match(string))
