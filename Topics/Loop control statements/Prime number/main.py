number = int(input())
is_prime = False
if number > 1:
    for n in range(2, number):
        if number % n == 0:
            break
    else:
        is_prime = True

if is_prime:
    print("This number is prime")
else:
    print("This number is not prime")
