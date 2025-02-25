from datetime import date
from endereco import Endereco
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    cpf: str
    data_nascimento: date
    endereco: Endereco


@dataclass
class PessoaRepository:
    dados: list[Pessoa]

    def buscar_todos(self):
        return self.dados

    def adicionar(self, pessoa: Pessoa):
        self.dados.append(pessoa)

    def buscar_pelo_cpf(self, cpf: str):
        for pessoa in self.dados:
            if pessoa.cpf == cpf:
                return pessoa
            
        return None
    
    def excluir_pelo_cpf(self, cpf: str):
        for i, pessoa in enumerate(self.dados):
            if pessoa.cpf == cpf:
                self.dados.pop(i)
    