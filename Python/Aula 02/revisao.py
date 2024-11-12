# Listas: Variaveis que podem armazenar varios valores de forma ordenada. Onde cada valor tem uma posição chamada indice
# Indices:       0       1        2
minha_lista = ['Davi', 'Wesley', 'Gabriel']

# Adicionando Elementos
minha_lista.append('Luiz')
# print(minha_lista)

# Iterando sobre a Lista
print('Nomes: ')
for nome in minha_lista:
    print(f'- {nome}')

# Procurar uma Informação
# Exemplo: Existe o nome 'John' na lista?
existe = False

for nome in minha_lista:
    if nome == 'John':
        existe = True
        break

if existe:
    print('O nome "John" existe na lista.')
else:
    print('O nome "John" não existe na lista.')

# Outra forma
# if 'John' in minha_lista:
#     print('O nome existe na lista.')
# else:
#     print('O nome não existe na lista.')
