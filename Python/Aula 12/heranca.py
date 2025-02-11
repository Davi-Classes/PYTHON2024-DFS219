# Herança
# A herança é a capacidade de uma classe de
# herdar os mesmos atributos e metódos de uma classe mãe
from conta import Conta


# Para herdar colocamos entre "()" a classe que estamos herdando.
class ContaCorrente(Conta):
    # Polimorfismo é a capacidade de sobreescrever 
    # um metódo herdado da classe mãe.
    def __init__(self, 
        titular: str, 
        saldo: float = 0, 
        cheque_especial: float = 0
    ):
        super().__init__(titular, saldo)
        self.cheque_especial = cheque_especial

    def sacar(self, valor: float):
        if valor <= 0:
            raise ValueError('O valor de saque deve ser positivo.')
        
        if self.saldo + self.cheque_especial < valor:
            raise ValueError('O valor de saque não pode ser maior que o saldo + cheque especial.')

        self.saldo -= valor


conta_corrente = ContaCorrente('Talia', 100, 50)

print(conta_corrente)
conta_corrente.sacar(160)
print(conta_corrente)