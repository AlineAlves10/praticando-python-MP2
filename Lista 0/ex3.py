numerotaxas = int(input())
taxa_maior = 0

for i in range(numerotaxas):
    taxas = float(input())
    if taxas > taxa_maior:
        taxa_maior = taxas

print(f"{taxa_maior:.2f}")