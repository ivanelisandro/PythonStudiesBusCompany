def check(text):
    if not text.isnumeric():
        print("It is not a number!")
        return
    number = int(text)
    required = 202
    if number >= required:
        print(number)
    else:
        print(f"There are less than {required} apples! You cheated me!")
