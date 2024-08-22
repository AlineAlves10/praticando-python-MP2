def slicing(lista, letra):
    if letra == 'R':
        lista.reverse()

    elif letra == 'S':
        fatia = input()
        com, fim = fatia.split()
        com = int(com)
        fim = int(fim) + 1
        teste = lista[com:fim]
        return teste
    return lista

lista = list(map(int, input().split()))
letra = input()

funcao = slicing(lista, letra)
print(funcao)