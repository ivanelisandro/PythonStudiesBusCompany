def grades(x):
    allowed = ('A', 'B', 'C', 'D', 'F')
    assert x in allowed
    return f'You have got {x}'
