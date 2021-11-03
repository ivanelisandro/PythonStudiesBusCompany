class NegativeSumError(Exception):
    def __init__(self):
        self.name = 'NegativeSumError'
        super().__init__()


def sum_with_exceptions(a, b):
    result = a + b
    if result < 0:
        raise NegativeSumError
    return result
