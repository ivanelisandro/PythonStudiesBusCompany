next_number = int(input())
total = next_number
total_squares = next_number ** 2

while total != 0:
    next_number = int(input())
    total += next_number
    total_squares += next_number ** 2

print(total_squares)
