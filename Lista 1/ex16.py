nome = input()
antes = input()
depois = input()

if antes == 'S':
    if depois == 'N':
        print(f'{nome} tinha interesse antes e não manteve interesse depois')
    else:
        print(f'{nome} tinha interesse antes e manteve interesse depois')
else:
    if depois == 'N':
        print(f'{nome} não tinha interesse antes e não teve interesse depois')
    else:
        print(f'{nome} não tinha interesse antes e teve interesse depois')    