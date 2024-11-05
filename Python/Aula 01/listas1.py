# Lista
# É uma estrutura ordenada, e indexada de forma posicional
#          0      1    2    3
lista = ['João', 6.7, 90, True]

# Acessar um valor
print(lista[0]) # 'João'
print(lista[2]) # 90

# Adicionar valores
lista.append(14) # Adiciona ao final da lista
lista.insert(0, 'Luiz') # Adiciona o elemento no indice informado.

# Excluir um elemento da lista
lista.pop() # Excluir o ultimo (14)
lista.pop(0) # Excluir o indice 0 ('Luiz')