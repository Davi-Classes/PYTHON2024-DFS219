from datetime import date, datetime
from dataclasses import dataclass


@dataclass
class Autor:
    nome: str
    data_nascimento: date

# tem o resultado abaixo:

# class Autor:
#     def __init__(self, nome: str, data_nascimento: date):
#         self.nome = nome
#         self.data_nascimento = data_nascimento


@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor

# tem o resultado abaixo:

# class Livro:
#     def __init__(self, titulo: str, ano: int, autor: Autor):
#         self.titulo = titulo
#         self.ano = ano
#         self.autor = autor

# Exemplo 1:
stephen_hawking = Autor('Stephen Hawking', date(day=8, month=1, year=1942))
print(stephen_hawking.nome.upper())
print(stephen_hawking.data_nascimento.year)

livro = Livro('Uma breve historia do Tempo', 1991, stephen_hawking)
print(livro.autor.data_nascimento.day)

# Exemplo 2:
nome = input('Digite o nome do Autor: ')
data_nascimento = input('Digite a data de nascimento (dd/MM/yyyy): ')

# Transformando a String em um Datetime, e pegando somente a parte da Data
data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date() 

print(data_nascimento)
autor = Autor(nome, data_nascimento)
print(autor)
