def create_dict():
    d = dict()
    key = 0
    def inner(*args):
        nonlocal key
        key +=1
        d.setdefault(key, *args)
        return d

    return inner


f_1 = create_dict()
print(f_1('hello')) # f_1   {1: 'hello'}
print(f_1(100)) # f_1   {1: 'hello', 2: 100}
print(f_1([1, 2, 3])) # f_1   {1: 'hello', 2: 100, 3: [1, 2, 3]}

f_2 = create_dict()
print(f_2('PoweR')) # f_2   {1: 'PoweR'}
