valor_produto = float(input())
valor_desconto = float(input())

soma = (valor_produto * valor_desconto) / 100
produto_descontado = valor_produto - soma

print('%.2f' % valor_produto)
print('%.2f' % produto_descontado)
print('%.2f' % soma)