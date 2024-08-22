adversativa = ['mas', 'porém', 'contudo', 'todavia', 'entretanto', 'no entanto', 'se não', 'não obstante', 'ainda assim', 'apesar disso', 'mesmo assim', 'de outra sorte', 'ao passo que']

frase = input()
frase_lista = frase.split()
adv = []

for i in frase_lista:
    if i in adversativa:
        adv.append(i)
        
if len(adv) == 0:
    print('não contém adversativa')
else:
    print(f'emprega: {", ".join(adv)}')