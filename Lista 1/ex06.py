cartas = []

for i in range(4):
    a = int(input())
    cartas.append(a)

carta_vencedora = max(cartas)

if cartas.count(carta_vencedora) > 1:
    print('empate')
else:
    print(carta_vencedora)
