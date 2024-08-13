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

