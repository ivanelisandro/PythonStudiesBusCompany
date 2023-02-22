numbers = input()
total = 0
total_list = []

for char in numbers:
    number = int(char)
    total += number
    total_list.append(total)

print(total_list)
