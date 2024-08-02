poema = input().lower()
d_palavras = {}
c = 0
for i in ['.', '"', ',', "'"]:
    poema = poema.replace(i, '')
poema = poema.split()

for i in poema:
    c = poema.count(i)
    d_palavras[i] = c

print(d_palavras)
palavra = input()
if palavra in d_palavras:
    vezes = d_palavras[palavra]
    print(vezes)
else:
    print(f'{palavra} não encontrada')

