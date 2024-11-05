# Listas com FOR
nomes = []

# Preencher
for i in range(1, 4):
    nome = input(f'Digite o nome do {i}º participante:')
    nomes.append(nome)

# Percorrer
print('---- Participantes ----')
for nome in nomes:
    print(f'- {nome}')