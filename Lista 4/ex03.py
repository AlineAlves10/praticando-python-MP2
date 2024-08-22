numeros = input().split()
lista = []
lista_ordenada = []

for i in numeros:
    lista.append(int(i))

while True:
    print('-', lista)
    print('+', lista_ordenada)

    menor = min(lista)
    lista.remove(menor)
    lista_ordenada.append(menor)

    if len(lista) == 0:
        print('-', lista)
        print('+', lista_ordenada)
        break


