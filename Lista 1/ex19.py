n_odio = int(input())
pais = input()
porc_odio = float(input())

soma = (n_odio * porc_odio) // 100
print(f'Triste número de mensagens de ódio à população LGBT+ no {pais} entre 2019 e 2022:')
print(f'%.0f' % soma)