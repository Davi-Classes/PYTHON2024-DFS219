class Cachorro:
    def __init__(self, nome: str, raca: str, idade: int):
        self.__validar(nome, raca, idade)
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f'O {self.nome} está latindo...')
    
    def aniversario(self):
        self.idade += 1

    # Metódo de Validação dos Parametros do Construtor
    def __validar(self, nome: str, raca: str, idade: int):
        if not isinstance(nome, str):
            raise ValueError('O nome deve ser uma string.')
        
        if not isinstance(raca, str):
            raise ValueError('A raça deve ser uma string.')

        if not isinstance(idade, int):
            raise ValueError('A idade deve ser um inteiro.')

# a.
c1 = Cachorro('Torby', 'Shitzu', 4)

# b.
c1.latir()

# c.
c2 = Cachorro('Lion', 'Chow-Chow', 7)

# d.
c2.latir()

# e.
print(c1.idade)
c1.aniversario()
print(c1.idade)