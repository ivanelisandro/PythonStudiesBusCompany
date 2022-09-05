# Don't download gutenberg corpus. Just import it
from nltk.corpus import gutenberg
whitman = gutenberg.sents('whitman-leaves.txt')
number = int(input())  # a row number of a sentence in Gutenberg corpus
print(whitman[number])
