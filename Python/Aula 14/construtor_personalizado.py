from datetime import date
from endereco import Endereco


class Pessoa:
    def __init__(self, 
        nome: str, cpf: str,data_nascimento: date, 
        cep: str, rua: str, numero: str, bairro: str, 
        cidade: str, estado: str, complemento: str | None = None
    ):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.endereco = Endereco(
            cep, rua, numero, bairro, cidade, estado, complemento
        )


pessoa = Pessoa(
    nome='Davi',
    cpf='12343443455',
    data_nascimento=date(2004, 1, 14),
    cep='41720000',
    rua='João José Rescala',
    numero='62',
    bairro='Imbuí',
    cidade='Salvador',
    estado='BA'
)

print(pessoa.nome)
print(pessoa.cpf)
print(pessoa.data_nascimento)
print(pessoa.endereco.formatar())