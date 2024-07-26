numero_exercicio = 1
versoes = [0, 0, 0, 0]
contador = 0

while numero_exercicio <= 4:
    resposta = input()
    contador += 1
    if resposta == "ok":
        versoes[numero_exercicio - 1] = contador
        contador = 0
        numero_exercicio += 1

print(f"Número de versões do primeiro exercício: {versoes[0]}")
print(f"Número de versões do segundo exercício: {versoes[1]}")
print(f"Número de versões do terceiro exercício: {versoes[2]}")
print(f"Número de versões do quarto exercício: {versoes[3]}")