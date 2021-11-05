from collections import Counter

words = input().lower().split()
counter = Counter(words)

print(sorted(counter.keys()))
