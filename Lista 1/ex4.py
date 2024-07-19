taxa_maior = 0

while True:
    taxas = float(input())
    if taxas > taxa_maior:
        taxa_maior = taxas
    elif taxas == 0:
        break

print(f"{taxa_maior:.2f}")