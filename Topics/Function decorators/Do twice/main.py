def do_twice(function):
    def wrapper(text):
        function(text)
        function(text)

    return wrapper
