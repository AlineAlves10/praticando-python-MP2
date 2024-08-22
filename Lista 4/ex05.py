itens_pessoais = ['vestido', 'camisa', 'camiseta', 'calça', 'bone']
itens_publicos = ['joia', 'arte', 'arma', 'veiculo']

itens_pe = []
itens_pu = []

while True:
    itens = input()
    if itens == '!':
        break
    elif itens in itens_pessoais:
        itens_pe.append(itens)
    elif itens in itens_publicos:
        itens_pu.append(itens)
    elif itens not in itens_pessoais and itens not in itens_publicos:
        itens_pu.append(itens)

print('itens pessoais:', len(itens_pe))
print('itens públicos:', len(itens_pu))