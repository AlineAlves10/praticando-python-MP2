nome = '0aline'
nome_novo = ''
nada = ''
for i in nome:
    if i == '0':
        nada += i
    else:
        nome_novo += i
    
print(nome_novo)

nome = 'Profa.Maria'
if nome.startswith('Profa. '): 
   nome = nome.replace('Profa. ', '')
print(nome)