num1 = int(input('Digite o 1º numero: '))
num2 = int(input('Digite o 2º numero: '))
num3 = int(input('Digite o 3º numero: '))

if num1 >= num2 and num1 >= num3:
    maior = num1
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

if num1 <= num2 and num1 <= num3:
    menor = num1
elif num2 <= num1 and num2 <= num3:
    menor = num2
else:
    menor = num3

print(f'O maior numero foi: {maior}')
print(f'O menor numero foi: {menor}')