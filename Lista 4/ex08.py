
lista = []
while True:
    string = input()
    if string == '.':
      break
    lista.append(string)

lista.sort()

tamanho = len(lista)
meio = len(lista) // 2

if tamanho % 2 == 0:
    print(lista[meio - 1])  
    print(lista[meio])      
else:
    print(lista[meio])