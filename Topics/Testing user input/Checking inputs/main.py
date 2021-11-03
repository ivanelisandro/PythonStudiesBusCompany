def check(x):
    number = None
    start = 120
    end = 137
    try:
        number = int(x)
    except ValueError:
        pass

    if number and start < number < end:
        print(number)
    else:
        print("That's a bad present!")
