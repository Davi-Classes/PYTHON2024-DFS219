# Criando Carro
carro = {}

carro['placa'] = input('Digite a placa do carro: ')
carro['marca'] = input('Digite a marca do carro: ')
carro['modelo'] = input('Digite a modelo do carro: ')
carro['cor'] = input('Digite a cor do carro: ')

# Mostrando dados do Carro
print('---- DADOS DO VEÍCULO ---')
print(f'Marca: {carro['marca']}')
print(f'Modelo: {carro['modelo']}')
print(f'Placa: {carro['placa']}')
print(f'Cor: {carro['cor']}')