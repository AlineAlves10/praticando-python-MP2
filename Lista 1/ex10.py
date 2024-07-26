conta = int(input())
compras = int(input())

soma = conta - compras
if compras <= conta:
    print(f'se você comprar tudo o saldo será:', soma)
else:
    print('seu saldo é insuficiente para essa compra')