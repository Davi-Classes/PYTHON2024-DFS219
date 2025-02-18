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
    
    # Diz como o objeto será convertido para "String"
    # É uma saida para o usuário
    def __str__(self) -> str:
        return self.formatar()

    # Diz como esse objeto será representado
    # É uma saida para o desenvolvedor
    def __repr__(self) -> str:
        return f'Endereco(rua="{self.rua}", numero="{self.numero}", ...)'

    def formatar(self):
        return f'{self.rua}, {self.numero} - {self.bairro} | {self.cidade} - {self.estado}, {self.cep}'
    

endereco = Endereco('12345-000', 'Av Contorno', 
    '1923', 'Savassi', 'Belo Horizonte', 'MG', 'Infinity School')


# Configuramos como o endereço é representado em STRING
endereco_em_str = str(endereco)
print(endereco_em_str)

# Representação
print(repr(endereco))
