def compute(x):
    a = x['GE Courses']
    b = x['Professional Courses']
    c = x['Core Courses']
    return sum(a.values()) + sum(b.values()) + sum(c.values())


def number_subjects(x):
    a = x['GE Courses']
    b = x['Professional Courses']
    c = x['Core Courses']

    return len(a.keys()) + len(b.keys()) + len(c.keys())


def display_subs(x):
    a = x['GE Courses']
    b = x['Professional Courses']
    c = x['Core Courses']
    print('--Subjects--')
    print('GE Courses')
    for n in a.keys():
        print(n)
    print('\n')
    print('Professional Courses')
    for n in b.keys():
        print(n)
    print('\n')
    print('Core Courses')
    for n in c.keys():
        print(n)
    print('\n')
