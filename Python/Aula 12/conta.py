# Programação Orientada a Objetos
# Classe:
# Uma representação abstrata de um conjunto de coisas que 
# possuem as mesmas caracteristicas (atributos) e comportamentos (metódos)
# Basicamente um molde para Criarmos Objetos a partir dele. 

# Coesão
# Uma classe coesa é uma classe onde a manipulação 
# das propriedades faz sentido. (Logicamente)
class Conta:
    # Metódo Construtor
    def __init__(self, titular: str, saldo: float = 0):
        if saldo < 0:
            raise ValueError('O saldo deve ser zerado ou positivo.')

        self.titular = titular
        self.saldo = saldo
    
    def saldo_formatado(self) -> str:
        valor = str(round(self.saldo, 2)).replace('.', ',')
        return f'R$ {valor}'

    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de deposíto deve ser positivo.')

        self.saldo += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de saque deve ser positivo.')
        
        if self.saldo < valor:
            raise ValueError('O valor de saque não pode ser maior que o saldo.')

        self.saldo -= valor

    def transferir(self, valor: float, conta: 'Conta'):
        self.sacar(valor)
        conta.depositar(valor)

    def __str__(self):
        return f'{self.titular} - {self.saldo_formatado()}'


# Exemplo de Utilização com Input.
# print('Cadastro Banco Infinity.')
# titular = input('Digite o titular da conta: ')

# conta = Conta(titular)

# valor_deposito = float(input('Quanto deseja depositar? '))
# conta.depositar(valor_deposito)
# print(f'Saldo da Conta: {conta.saldo_formatado()}')

# valor_saque = float(input('Quanto deseja sacar? '))
# conta.sacar(valor_saque)
# print(f'Saldo da Conta: {conta.saldo_formatado()}')

# c1 = Conta('Davi', 100)
# c2 = Conta('Fernanda', 30)

# print(c1)
# print(c2)

# c1.transferir(80, c2)

# print(c1.saldo_formatado())
# print(c2.saldo_formatado())