# POO
# Uma classe é uma representação abstrata
# de um conjunto de "coisas" que possuem 
# as mesmas caracteristicas (atributos) e comportamentos (metódos)

# "Se algo é um objeto, ele tem atributos e metódos."
class Carro:
    # Metódo Construtor
    def __init__(
        self, marca: str, modelo: str, placa: str, cor: str
    ):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa
        self.cor = cor
        self.ligado = False

    def info(self):
        print('---- DADOS DO VEÍCULO ---')
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Placa: {self.placa}')
        print(f'Cor: {self.cor}')


# Criando o Carro
carro1 = Carro('Honda', 'Civic', 'CCC0C22', 'Vermelho')

# Acessando Propriedades do Carro
# utilizando o ".<atributo>" você acessa a propriedade desejada
print(carro1.marca)
print(carro1.modelo)
print(carro1.placa)

# Chamando Metódos
# carro1.info()

carro2 = Carro('Chevrolet', 'Celta', 'AAA1A11', 'Prata')
# carro2.info()