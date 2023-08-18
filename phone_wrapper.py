import operator

def person_lister(f):
    def inner(people):
        # complete the function
        people.sort(key=lambda x: x[2])
        return [f(person) for person in people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [
        'Jake Jake 42 M',
'Jake Kevin 57 M',
'Jake Michael 91 M',
'Kevin Jake 2 M',
'Kevin Kevin 44 M',
'Kevin Michael 100 M',
'Michael Jake 4 M',
'Michael Kevin 36 M',
'Michael Michael 15 M',
'Micheal Micheal 6 M',
    ]
    print(*name_format(people), sep='\n')