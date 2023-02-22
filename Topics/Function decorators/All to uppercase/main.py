def to_upper(function):
    def wrapper(text):
        return function(text.upper())

    return wrapper
