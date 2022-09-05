number = int(input())
number_bytes = number.to_bytes(2, "big")
print(sum(number_bytes))
