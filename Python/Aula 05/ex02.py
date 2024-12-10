def verificar_par(numero: int) -> bool:
    return numero % 2 == 0


n = int(input('Digite um numero: '))

if verificar_par(n):
    print('O numero é par.')
else:
    print('O numero não é par.')