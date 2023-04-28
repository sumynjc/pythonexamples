def read(s:str, end='end'):
    res = {}
    while s !=end:
        key, value = s.split(': ')
        res.setdefault(key, set()).add(value)
        s = input()
    return res

def view(d:dict):
    for item in sorted(d.items(), key=lambda pair: len(pair[1]), reverse=True):
        print(f"The number of unique commentators at the {item[0]} - {len(item[1])}")

view(read(input()))
