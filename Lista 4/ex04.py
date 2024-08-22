def binary_extraction(lista, ext):
    nova_lista = []
    for i in range(ext):
        meio = len(lista) // 2
        nova_lista.append(lista[meio])
        lista.pop(meio)

    return nova_lista

lista = list(map(int, input().split()))
extracao = int(input())
print(lista)
nova = binary_extraction(lista, extracao)
print(nova)