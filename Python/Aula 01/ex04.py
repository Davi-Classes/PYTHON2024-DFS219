pares = []
impares = []
numeros = []

for n in range(1, 7):
    numero = int(input(f'Digite o {n}º valor: '))
    numeros.append(numero)

    # Vocês podem fazer a separação aqui
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'Numeros: {numeros}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')

# Ou realizar a separação depois que os dados foram inseridos.
# for numero in numeros:
#     if numero % 2 == 0:
#         pares.append(numero)
#     else:
#         impares.append(numero)