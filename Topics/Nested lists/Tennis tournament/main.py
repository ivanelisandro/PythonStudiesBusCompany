number = int(input())
names = []
victories = 0

while number > 0:
    (name, result) = input().split()
    if result == 'win':
        names.append(name)
        victories += 1
    number -= 1

print(names)
print(victories)
