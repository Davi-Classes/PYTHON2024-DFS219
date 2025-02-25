from dataclasses import dataclass


@dataclass
class Endereco:
    cep: str 
    rua: str 
    numero: str
    bairro: str 
    cidade: str 
    estado: str 
    complemento: str | None = None

    def __str__(self):
        return self.formatar()
    
    def __repr__(self):
        return self.formatar()

    def formatar(self):
        return f'{self.rua}, {self.numero} - {self.bairro} | {self.cidade} - {self.estado}, {self.cep}'
    
