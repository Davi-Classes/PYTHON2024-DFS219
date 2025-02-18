# Ex01. Crie uma classe "Pessoa" que deve conter:

# Atributos
# - nome (str)
# - data_nascimento (date)
# - endereco (Endereco)

# A propriedade "endereco" será uma outra classe "Endereco" que terá:

# Atributos
# - cep (str)
# - rua (str)
# - numero (str)
# - bairro (str)
# - cidade (str)
# - estado (str)
# - complemento (str)

# Metódos:
# - formatar() | Retorna o endereço formatado em uma String

# A formatação será:
# "Rua, Numero - Bairro | Cidade - Estado, Cep"
from datetime import date


class Endereco:
    def __init__(self, 
        cep: str, rua: str, numero: str, bairro: str, 
        cidade: str, estado: str, complemento: str | None = None
    ):
        self.cep = cep
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.complemento = complemento
    
    def formatar(self):
        return f'{self.rua}, {self.numero} - {self.bairro} | {self.cidade} - {self.estado}, {self.cep}'
    
class Pessoa:
    def __init__(self, nome: str, data_nascimento: date, endereco: Endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.endereco = endereco

endereco = Endereco('12345-000', 'Av Contorno', 
    '1923', 'Savassi', 'Belo Horizonte', 'MG', 'Infinity School')

pessoa = Pessoa('Pedro K.', date(1990, 4, 13), endereco)

print(pessoa.nome)
print(pessoa.data_nascimento)
print(pessoa)
print(pessoa.endereco)