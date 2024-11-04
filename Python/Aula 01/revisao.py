# Entrada
# Variavel -> Inteira
ano = int(input('Digite o ano: ')) # Casting


# Processamento
# Condicionais -> Operadores Relacionais
bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

# Saída
if bissexto:
    print('O ano é bissexto.')
else:
    print('O ano não é bissexto.')