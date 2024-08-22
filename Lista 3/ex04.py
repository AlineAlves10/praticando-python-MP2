def my_pesquisa_binaria(lista, valor_procurado):
    esquerda  = 0
    direita = len(lista) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        print(lista[esquerda:direita+1])
        
        if lista[meio] == valor_procurado:
            print(f"Encontrado na posição {meio}")
            return meio
        
        elif lista[meio] > valor_procurado:
            direita = meio - 1
        
        else:
            esquerda = meio + 1
    
    print("Elemento não encontrado", valor_procurado)
    return -1

lista = input().split()
valor_procurado = input()

my_pesquisa_binaria(lista, valor_procurado)