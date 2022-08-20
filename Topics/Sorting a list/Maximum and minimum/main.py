# the following code creates a list from input, please do not modify it
ints = [int(num) for num in input().split()]
(minimum, middle, maximum) = sorted(ints)
print(maximum, minimum, middle)
