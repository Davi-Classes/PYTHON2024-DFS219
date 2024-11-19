estoque = {"banana": 10, "laranja": 5, "uva": 8}

print('Estoque Antigo')
for fruta, quantidade in estoque.items():
    print(f'- {fruta} x {quantidade}')

print('------------------------')

# Removeu a Laranja.
estoque.pop('laranja')

print('Estoque Atualizado')
for fruta, quantidade in estoque.items():
    print(f'- {fruta} x {quantidade}')