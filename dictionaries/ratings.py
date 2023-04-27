def read(s, end='end'):
    res = dict()
    while s !=end:
        key, value = s.split(', ')
        res.setdefault(key, []).append(int(value))
        s = input()
    return res

def take_ratings(d:dict):
    res = dict()
    for key in sorted(d):
        rating = sum(d[key])/len(d[key])
        res.setdefault(key, rating)

    return res

def view(d:dict):
    for item in sorted(d.items(), key=lambda pair: pair[1], reverse=True):
        print(f"{item[0]} {item[1]}")

view(take_ratings(read(input())))
