# Dicionarios
carro = {
    # Chave: Valor
    'placa': 'DER1234', # Item
    'modelo': 'Celta',
    'marca': 'Chevrolet',
    'ano': 2010
}

# placa = 'DER1234'
# modelo = 'Celta'
# marca = 'Chevrolet'
# ano = 2010

# Buscar Informações.
# dicionario.get(<chave>)
print(f'Placa: {carro.get("placa")}')
# ou
# dicionario[<chave>]
print('Modelo: ' + carro['modelo'])
print(carro)

# Criar ou Atualizar Valores
# dicionario[<chave>] = <valor>
carro['uso'] = int(input('Quanto de uso o carro tem (em KM)? '))
print(carro)
