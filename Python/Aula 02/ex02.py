pessoas = {
    'Lidia': 21,
    'Gabriel': 20,
    'Walter': 24,
    'Caio': 24,
    'Enzo': 22
}

for n in range(1, 4):
    nome = input('Digite o nome de uma pessoa: ')
    idade = int(input('Digite a idade da pessoa: '))

    pessoas[nome] = idade

print('Todas as Pessoas: ')
for nome, idade in pessoas.items():
    print(f'- {nome} ({idade} Anos)')
