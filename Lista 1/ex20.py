pais = input()
n_odio = float(input())

pais2 = input()
n_odio2 = float(input())

if n_odio > n_odio2:
    print(f'{pais} > {pais2}')
elif n_odio2 > n_odio:
    print(f'{pais2} > {pais}')
elif n_odio == n_odio2:
    print(f'{pais} = {pais2}')