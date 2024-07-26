qts_alunas = int(input())
c = 0
for i in range(qts_alunas):
    notas = int(input())
    c += notas
soma = c / qts_alunas
print(f'média %.1f' % soma)