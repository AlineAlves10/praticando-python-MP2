#criptografia
#Na primeira, o caractere a ser trocado. 
#Na segunda linha, o caractere que irá substituir o caractere a ser trocado. 
#Na terceira linha, a mensagem a ser criptografada.

caractere = input()
substituir = input()
mensagem = input()

mensa = ""
for i in mensagem:
    if i == caractere:
        mensa += substituir 
    else:
        mensa += i
print(mensa)