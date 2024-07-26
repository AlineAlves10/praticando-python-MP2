n_alunas = int(input())
aprovadas = int(input())

soma = ((aprovadas * 100) / n_alunas) / 100
print(f'a taxa de aprovação é %.2f' % soma)