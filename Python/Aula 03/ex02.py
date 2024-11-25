# Entrada
modelo = input('Digite o modelo do carro: ')
ano = int(input('Digite o ano do carro: '))
preco_fip = float(input('Digite o preço da tabela fip: '))
uso_km = float(input('Digite a kilometragem do carro: '))

# Processamento
if uso_km > 300_000:
    preco_venda = preco_fip * (1 - 0.5)
elif uso_km > 200_000: 
    preco_venda = preco_fip * (1 - 0.35)
elif uso_km > 150_000:
    preco_venda = preco_fip * (1 - 0.3)
elif uso_km > 100_000:
    preco_venda = preco_fip * (1 - 0.2)
else:
    preco_venda = preco_fip * (1 - 0.15)

# Saída
print(f'Modelo: {modelo}')
print(f'Ano: {ano}')
print(f'Uso (Km): {uso_km}')
print(f'Preço Tabela Fip: {preco_fip}')
print(f'Preço de Venda: {preco_venda}')