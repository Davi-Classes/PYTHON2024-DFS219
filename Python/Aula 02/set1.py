# Sets (Conjuntos)
# Conjuntos não são ordenados
# Conjuntos não contem elementos duplicados
conjunto = {1, 4, 5, 6, 3, 1}

# Operacoes
a = {'Luiz', 'Roberto'}
b = {'Gabriel', 'Thiago'}

# print(a)
# print(b)

# União
print(a.union(b))

# Intersecção
print(a.intersection(b))

# Removendo Duplicados de uma Lista
nomes = ['Lidia', 'Rafael', 'Caio', 'Caio', 'Lidia']
print(nomes)

nomes_sem_duplicados = list(set(nomes))
nomes_sem_duplicados.sort() # Ordenar

print(nomes_sem_duplicados)