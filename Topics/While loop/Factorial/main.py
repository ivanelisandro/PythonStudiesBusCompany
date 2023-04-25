number = int(input())
factorial = number

while number > 1:
    number -= 1
    factorial *= number

print(factorial)
