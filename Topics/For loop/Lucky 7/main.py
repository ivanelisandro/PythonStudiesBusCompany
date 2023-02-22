quantity = int(input())
lucky_number = 7

while quantity > 0:
    number = int(input())
    if number % lucky_number == 0:
        print(number ** 2)
    quantity -= 1
