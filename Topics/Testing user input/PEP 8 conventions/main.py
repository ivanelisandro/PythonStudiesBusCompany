def check_name(name):
    forbidden = ('l', 'I', 'O')
    if name in forbidden:
        print("Never use the characters 'l', 'O', or 'I' as single-character variable names")
    elif name.islower():
        print("It is a common variable")
    elif name.isupper():
        print("It is a constant")
    else:
        print("You shouldn't use mixedCase")
