# Encapsulamento

# O encapsulamento se trata sobre controle de acesso
# aos atributos e metódos de uma classe

# Tipos de Visibilidade
# - Publica (Pode ser acessado fora da classe)
# - Protegido (Pode ser acessado somente dentro da propria classe ou das suas subclasses)
# - Privado (Pode ser acessado somente dentro da propria classe)

class Conta:
    def __init__(self, titular: str, saldo: float = 0):
        if saldo < 0:
            raise ValueError('O saldo deve ser zerado ou positivo.')

        self.titular = titular
        self.__saldo = saldo
    
    # Getter (Comum)
    def get_saldo(self):
        return self.__saldo
    
    def saldo_formatado(self) -> str:
        valor = str(round(self.__saldo, 2)).replace('.', ',')
        return f'R$ {valor}'

    # Setters
    def depositar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de deposíto deve ser positivo.')

        self.__saldo += valor

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de saque deve ser positivo.')
        
        if self.__saldo < valor:
            raise ValueError('O valor de saque não pode ser maior que o saldo.')

        self.__saldo -= valor

    def transferir(self, valor: float, conta: 'Conta'):
        self.sacar(valor)
        conta.depositar(valor)

    def __str__(self):
        return f'{self.titular} - {self.saldo_formatado()}'


conta = Conta('Davi', 200)
print(conta)

conta.__saldo = conta.get_saldo() - 1000
# conta.sacar(300)

print(conta)