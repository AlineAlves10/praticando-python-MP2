adversativa = ('mas', 'porem', 'contudo', 'todavia', 'entretanto', 'no entanto', 'se não', 'não obstante', 'ainda assim', 'apesar disso', 'mesmo assim', 'de outra sorte', 'ao passo que')

string = input()

if string in adversativa:
    print('reconheço como conjunção adversativa')
else:
    print('não reconheço como conjunção adversativa')