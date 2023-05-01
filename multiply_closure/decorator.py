def text_decor(func):

    def inner(*args, **kvargs):
        print("Hello")
        func(*args, **kvargs)
        print("Goodbye!")

    return inner


@text_decor
def simple_func():
    print('I just simple python func')

@text_decor
def multiply(num1, num2):
    print(num1 * num2)


simple_func()
multiply(3, 5)
