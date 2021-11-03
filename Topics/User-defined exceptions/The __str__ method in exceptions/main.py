# NotInBoundsError is predefined
def check_integer(num):
    start = 45
    end = 67
    if start < num < end:
        return num
    raise NotInBoundsError


def error_handling(num):
    try:
        print(check_integer(num))
    except NotInBoundsError as error:
        print(error)
