salarios = {
    "gerente": 5000, 
    "analista": 4000, 
    "desenvolvedor": 3500, 
    "estagiário": 1500
}

total = 0
for salario in salarios.values():
    # total = total + salario
    total += salario

print(total)
print(sum(salario.values()))

# # Buscando as chaves
# print(salarios.keys())

# # Buscando os Valores
# print(salarios.values())