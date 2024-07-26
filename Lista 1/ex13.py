linha = input()

l_strings = []
for s in linha.split():
  l_strings.append(s)

l_inteiros = []
for i in linha.split():
  i = int(i)
  l_inteiros.append(i * 2)

l_decimais = []
for f in linha.split():
  f = float(f)
  l_decimais.append(f / 2)

print(l_strings)
print(l_inteiros)
print(l_decimais)
print(len(l_inteiros))