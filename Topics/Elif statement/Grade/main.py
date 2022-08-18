score = int(input())
maximum = int(input())

ratio = score / maximum

grades = {
    'A': (0.9, 1),
    'B': (0.8, 0.9),
    'C': (0.7, 0.8),
    'D': (0.6, 0.7),
    'F': (0, 0.6),
}

for key, value in grades.items():
    start, end = value
    if start <= ratio < end:
        print(key)
