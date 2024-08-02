#ignorando a pontuação, as aspas simples e as aspas duplas,

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
