conta = float(input("Digite o valor da sua conta:"))
juros = float(input("Valor do juros mensal:"))

soma = (conta * juros)/100
print("{:.2f}".format(conta + soma))