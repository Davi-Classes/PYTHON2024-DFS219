# Ex03. Faça uma função chamada "calcular_area_retangulo" que recebe dois parametros ("base" e "altura") e retorna a area do retangulo.

def calcular_area_retangulo(base, altura):
    area = base * altura
    return area


base1 = float(input('Digite a base: '))
altura1 = float(input('Digite a altura: '))

area1 = calcular_area_retangulo(base1, altura1)
print(f'A area do retangulo é: {area1}m²')