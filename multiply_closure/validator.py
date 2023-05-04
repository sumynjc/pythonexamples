from functools import wraps

def validate_args(f):

    @wraps(f)
    def inner(*args):
        ln = 2
        if len(args) < ln:
            return "Not enough arguments"
        if len(args) > ln:
            return "Too many arguments"
        for a in args:
            if not isinstance(a, int):
                return "Wrong types"

        return f(*args)

    return inner


@validate_args
def add_numbers(x, y):
    """Return sum of x and y"""
    return x + y


assert add_numbers(4, 5) == 9
assert add_numbers(4) == 'Not enough arguments'
assert add_numbers() == 'Not enough arguments'
assert add_numbers('hello') == 'Not enough arguments'
assert add_numbers(3, 5, 6) == 'Too many arguments'
assert add_numbers('a', 'b', 'c') == 'Too many arguments'
assert add_numbers(4.5, 5.1) == 'Wrong types'
assert add_numbers('hello', 4) == 'Wrong types'
assert add_numbers(9, 'hello') == 'Wrong types'
assert add_numbers([1, 3], {}) == 'Wrong types'
assert add_numbers.__name__ == 'add_numbers'
assert add_numbers.__doc__.strip() == 'Return sum of x and y'
print('Good')
