from functools import wraps

def add_args(f):
    @wraps(f)
    def inner(*args, **kwargs):
        args = 'begin', *args, 'end'
        return f(*args, **kwargs)

    return inner


@add_args
def concatenate(*args):
    """
    Returns the concatenation of the input lines
    """
    return ', '.join(args)


@add_args
def find_max_word(*args):
    """
    Returns the maximum length of the word
    """
    return max(args, key=len)


print(concatenate('hello', 'world', 'my', 'name is', 'Artem'))
assert concatenate('hello', 'world', 'my', 'name is', 'Artem') == 'begin, hello, world, my, name is, Artem, end'
assert concatenate('my', 'name is', 'Artem') == 'begin, my, name is, Artem, end'
assert concatenate.__name__ == 'concatenate'
assert concatenate.__doc__.strip() == """Returns the concatenation of the input lines"""
assert find_max_word('my') == 'begin'
assert find_max_word('my', 'how') == 'begin'
assert find_max_word('my', 'how', 'maximum') == 'maximum'
assert find_max_word.__name__ == 'find_max_word'
assert find_max_word.__doc__.strip() == """Returns the maximum length of the word"""
