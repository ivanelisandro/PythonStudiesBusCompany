names = input().split()
names = sorted(set(names))

print(*names, sep='\n')
