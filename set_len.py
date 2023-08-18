a = 10
s = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
ran = 15
comands = [
    'remove 1',
    'pop',
    'pop',
    'discard 2',
    'discard 3',
    'discard 4',
    'discard 1',
    'remove 5',
    'pop',
    'discard 6',
    'discard 1',
    'discard 8',
    'discard 0',
    'discard 9',
    'pop'
]

for comand in comands:
    code = comand.split()
    # try:
    if 'pop' in code:
        s.pop()
    else:
        # try:
        comand = code[0]
        num = code[1]
        comand = 's.' + comand + '(' + str(num) + ')'
        print(comand)
        eval(comand)
        # except Exception:
            # pass
    
print(len(s))
