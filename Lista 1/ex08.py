
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
    print(f"  Alimentação: %.2f" % a)
if m != 0:
    print(f"  Moradia: %.2f" % m)
if t != 0:
    print(f"  Transporte: %.2f" % t)
if s != 0:
    print(f"  Saúde: %.2f" % s)
if l != 0:
    print(f"  Lazer: %.2f" % l)
if sa != 0:
    print(f"  Salário: %.2f" % sa)
if p != 0:
    print(f"  Prestação de serviços: %.2f" % p)

print(f"Total de Renda: %.2f" % total_renda)
print(f"Total de Gastos: %.2f" % total_gastos)
print(f"Balanço: %.2f" % balanco)
