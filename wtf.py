def myf(d, barney={}):
    if d not in barney.keys():
        barney[d] = 1
    else:
        barney[d] += 1
    for k, v in barney.items():
        print(f'{k}: {v}')
    print()
#
myf('a')
myf('a')
myf('b')
#
myf('y', {})
myf('y', {})
myf('z', {})
