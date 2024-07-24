qtd_movimentação = int(input())
c = 0

for i in range(qtd_movimentação):
    n_moviment = float(input())
    c += n_moviment

print('%.2f' % c)