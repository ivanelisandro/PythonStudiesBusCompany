scores = input().split()
correct_count = 0
incorrect_count = 0

for answer in scores:
    if answer == 'C':
        correct_count += 1
    if answer == 'I':
        incorrect_count += 1
    if incorrect_count == 3:
        print('Game over')
        break
else:
    print('You won')

print(correct_count)
