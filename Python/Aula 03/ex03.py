numeros = []

# Entrada
while True:
    num = int(input('Digite um numero: '))
    numeros.append(num)

    resp = input('Deseja Continuar [S/N]?  -> ')

    if resp.lower() == 'n':
        break

# Processamento
maior = menor = numeros[0]
for numero in numeros:
    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

# Saída
print(f'Numeros Digitados: {numeros}')
print(f'Maior Numero: {maior}')
print(f'Menor Numero: {menor}')