class WordError(Exception):
    def __init__(self):
        self.name = 'WordError'
        super().__init__()


def check_w_letter(word):
    if 'w' in word:
        raise WordError
    return word
