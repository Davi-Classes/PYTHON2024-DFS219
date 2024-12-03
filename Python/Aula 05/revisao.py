# Funções
# Ao definir uma função utilizamos a palavra reservada "def" com a seguinte sintaxe:

# def minha_funcao(parametro1, parametro2...):
#   ... corpo da função
#   return resultado

# Entrada: Parametros
# Processamento: Corpo da Função
# Saída: Resultado
def somar(n1, n2):
    return n1 + n2

# Utilizar a função
numero1 = int(input('Digite um numero: '))
numero2 = int(input('Digite outro numero: '))

# Chamando a função "somar" passando os parametros de forma posicional
resultado1 = somar(1, 13)
resultado2 = somar(numero1, numero2)

print(f'Resultado 1: {resultado1}')
print(f'Resultado 2: {resultado2}')
print(f'Resultado 2: {resultado2}')