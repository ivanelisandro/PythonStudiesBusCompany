def add_underscores(word):
    new_word = '_'.join(word)
    return f'_{new_word}_'


text = input()
print(add_underscores(text))
