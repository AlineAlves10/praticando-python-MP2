
a = 0
m = 0
t = 0
s = 0
l = 0
sa = 0
p = 0

qtd = int(input())

for i in range(qtd):
    valor = float(input())
    letra = input()
    if letra == 'A':
        a += valor
    elif letra == 'M':
        m += valor
    elif letra == 'T':
        t += valor
    elif letra == 'S' and valor < 0:
        s += valor
    elif letra == 'L':
        l += valor
    elif letra == 'S' and valor > 0:
        sa += valor
    elif letra == 'P':
        p += valor

total_gastos = a + m + t + s + l
total_renda = p + sa
balanco = total_gastos + total_renda 

total_gastos = a + m + t + s + l
total_renda = p + sa
balanco = total_renda + total_gastos

print("Movimentações")
if a != 0:
    print(f"Alimentação: {a:.2f}")
if m != 0:
    print(f"Moradia: {m:.2f}")
if t != 0:
    print(f"Transporte: {t:.2f}")
if s != 0:
    print(f"Saúde: {s:.2f}")
if l != 0:
    print(f"Lazer: {l:.2f}")
if sa != 0:
    print(f"Salário: {sa:.2f}")
if p != 0:
    print(f"Prestação de serviços: {p:.2f}")

print(f"Total de Renda: {total_renda:.2f}")
print(f"Total de Gastos: {total_gastos:.2f}")
print(f"Balanço: {balanco:.2f}")
