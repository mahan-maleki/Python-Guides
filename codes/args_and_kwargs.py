# Args:
def jam(*args):
    print(args)

    res = 0

    for i in args:
        res += i

    return res

print(jam(1,2,3,4,5))

# KwArgs:
def masahat(**kwargs):
    if 'tool' in kwargs:
        return kwargs['tool'] * kwargs['ertefa']
    if 'shoa' in kwargs:
        return kwargs['shoa'] ** 2 * 3

masahat(tool=8, ertefa=7)