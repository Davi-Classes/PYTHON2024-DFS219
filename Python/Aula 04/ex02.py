# Ex02. Faça uma função "calcular_salario" que recebe um parametro "salario" e retorna o salario deduzido das seguintes taxas:

# - IR: 8%
# - INSS: 5%
# - Sindicato: 3%

# Definição
def calcular_salario(salario):
    ir = 0.08
    inss = 0.05
    sindicato = 0.03

    salario_liquido = salario * (1 - ir - inss - sindicato)
    return salario_liquido


# Utilização
salario_gerente = float(input('Digite o salário do gerente: '))
salario_supervisor = float(input('Digite o salário do supervisor: '))

salario_gerente = calcular_salario(salario_gerente)
salario_supervisor = calcular_salario(salario_supervisor)

print(f'O salário liquido do gerente é: {salario_gerente}')
print(f'O salário liquido do supervisor é: {salario_supervisor}')