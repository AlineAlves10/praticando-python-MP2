ano = int(input())

if ano >= 1932 and ano < 1946:
    print('voto facultativo para mulheres')
elif ano >= 1946:
    print('voto obrigatório para mulheres')
else:
    print('mulheres proibidas de votar')