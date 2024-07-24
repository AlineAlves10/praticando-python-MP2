#.isalnum()
#um nome de variável pode conter apenas caracteres alfanuméricos e o underscore (a-z, A_Z, 0-9, _ )
#um nome de variável deve começar com uma letra ou o caractere de underscore '_'

nome_variavel = input()
e = False
for i in nome_variavel:
    if not i.isalnum() and i != '_':
        e = True
if nome_variavel[0].isalpha() or nome_variavel[0] == "_":
    if not e:
        print('ok')
    else:
        print('ERROR')
else:
    print('ERROR')