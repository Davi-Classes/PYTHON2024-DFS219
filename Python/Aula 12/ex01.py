# Ex01. Crie uma classe chamada "Funcionario" que deve ter os atributos e metódos:

# Atributos:
# - nome
# - salario

# Metódos:
# - calcular_salario()

# O calcular salário deve retornar o salario com uma dedução de 3%.

class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario
    
    def calcular_salario(self):
        imposto = 0.03
        return self.salario - (self.salario * imposto)

    def info(self):
        print(f'Funcionario: {self.nome}')
        print(f'Salario Bruto: {self.salario}')
        print(f'Salario Liquido: {self.calcular_salario()}')

# a. Crie uma classe "Gerente" que deve ter os mesmos atributos do Funcionário, mas a dedução do salário deve ser de 11% no "calcular_salario()".

# nome = input('Digite o nome do funcionário: ')
# salario = float(input('Digite o salário do funcionário: '))

# funcionario = Funcionario(nome, salario)

# funcionario.info()

class Gerente(Funcionario):
    def calcular_salario(self):
        imposto = 0.11
        return self.salario - (self.salario * imposto)


# nome = input('Digite o nome do funcionário: ')
# salario = float(input('Digite o salário do funcionário: '))

# funcionario = Gerente(nome, salario)

# funcionario.info()

# b. Crie uma classe "Vendedor" que deve ter um atributo de "comissao: float", que será informado no construtor. O salario deve ter uma dedução de 8% "calcular_salario()" mas deve somar o valor da comissão.

class Vendedor(Funcionario):
    def __init__(self, nome: str, salario: float, comissao: float = 0):
        super().__init__(nome, salario)
        self.comissao = comissao

    def calcular_salario(self):
        imposto = 0.08
        total = self.salario + self.comissao
        return total - (total * imposto)
    
    def info(self):
        super().info()
        print(f'Comissão: {self.comissao}')
    

nome = input('Digite o nome do funcionário: ')
salario = float(input('Digite o salário do funcionário: '))
comissao = float(input('Digite a comissão do funcionário: '))

funcionario = Vendedor(nome, salario, comissao)

print(funcionario.calcular_salario())

