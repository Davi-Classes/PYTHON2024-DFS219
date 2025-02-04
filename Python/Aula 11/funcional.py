# Pedindo Dados
def pedir_dados_carro():
    marca = input('Digite a marca do carro: ')
    modelo = input('Digite a modelo do carro: ')
    placa = input('Digite a placa do carro: ')
    cor = input('Digite a cor do carro: ')

    return marca, modelo, placa, cor


# Criando Carro
def criar_carro(
    marca: str, modelo: str, placa: str, cor: str
) -> dict:
    return {
        'marca': marca,
        'modelo': modelo,
        'placa': placa,
        'cor': cor
    }


# Mostrando dados do Carro
def info_carro(carro: dict):
    print('---- DADOS DO VEÍCULO ---')
    print(f'Marca: {carro['marca']}')
    print(f'Modelo: {carro['modelo']}')
    print(f'Placa: {carro['placa']}')
    print(f'Cor: {carro['cor']}')


# marca, modelo, placa, cor = pedir_dados_carro()
# carro1 = criar_carro(marca, modelo, placa, cor)
# info_carro(carro1)

carro2 = criar_carro('Honda', 'Civic', 'CCC0C22', 'Vermelho')
info_carro(carro2)

# A chave não vai existir, e fica dependendo do programador
# Conhecer todas as chaves.
if carro2.get('marcar') == 'Peugeot':
    # Faça alguma coisa...
    pass