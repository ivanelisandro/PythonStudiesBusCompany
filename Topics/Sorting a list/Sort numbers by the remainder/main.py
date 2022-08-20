nums = [int(number) for number in list(input())]

print(sorted(nums, key=lambda x: x % 3))
