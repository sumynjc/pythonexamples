def repeater(f):
    def inner(*args):
        f(*args)
        f(*args)
    return inner

@repeater
def multiply(num1, num2):
    print(num1 * num2)

multiply(2, 7)
multiply(5, 3)
