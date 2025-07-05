# TODO: Create the logging_decorator() function 👇


# TODO: Use the decorator 👇

def logging_decorator(function):
    def wrapper(*args):
        returned_value = function(*args)

        print(f"You called {function.__name__}{args}")
        print(f"It returned: {returned_value}")
        return returned_value

    return wrapper


@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)