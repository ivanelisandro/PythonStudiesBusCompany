def check():
    number = None
    start = 25
    end = 37
    try:
        number = int(input())
    except ValueError:
        pass

    if number and start <= number <= end:
        print(number)
    else:
        print("Correct the error!")
