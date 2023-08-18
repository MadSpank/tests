from itertools import groupby

s = '1222311'

result = ''

for item, iter in groupby(s):
    result += f'({len(list(iter))}, {item}) '

print(result)