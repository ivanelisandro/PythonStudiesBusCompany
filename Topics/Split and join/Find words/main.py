words = input()
selection = [word for word in words.split() if word.endswith('s')]
print(*selection, sep='_')
