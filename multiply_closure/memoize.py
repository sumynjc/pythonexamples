from functools import wraps

def memoize(f):

    d = [0,1,1,2,3,5,8,13,21]
    @wraps(f)
    def inner(*args):
        if args[0] >= len(d):
            d.append(f(*args))
            return d[-1]
        else:
            return d[args[0]]

    return inner



@memoize
def fibonacci(n):
    """
    Returns the nth Fibonacci number
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


assert fibonacci(50) == 12586269025
assert fibonacci(60) == 1548008755920
assert fibonacci(70) == 190392490709135
assert fibonacci(80) == 23416728348467685
assert fibonacci(90) == 2880067194370816120
assert fibonacci(100) == 354224848179261915075
assert fibonacci.__name__ == 'fibonacci'
assert fibonacci.__doc__.strip() == 'Returns the nth Fibonacci number'
print('Good')
