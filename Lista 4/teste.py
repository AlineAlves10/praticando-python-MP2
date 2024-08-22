def slicing(palavra, num1, num2):
    string = palavra
    teste = string[num1:num2]
    return teste

frase = input()
fatia = input()
com, fim = fatia.split()
com = int(com)
fim = int(fim)

a = slicing(frase, com, fim)
print(a)



def slicing(palavra, num1, num2, num3):
    string = palavra
    teste = string[num1:num2:num3]
    return teste

frase = input()
fatia = input()
com, fim, passo = fatia.split()
com = int(com)
fim = int(fim)
passo = int(passo)

a = slicing(frase, com, fim, passo)
print(a)