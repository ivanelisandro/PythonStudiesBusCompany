start = int(input())
end = int(input())
cycles_to_days = 12

cycles = 0
while start > end:
    cycles += 1
    start /= 2

print(cycles * cycles_to_days)
