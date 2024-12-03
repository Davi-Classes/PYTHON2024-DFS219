# Ex04. Você foi contratado por uma instituição de nutrição para ajuda-los em um sistema:

# a. Faça uma função chamada "calcular_imc" que irá receber dois parametros ("peso" e "altura") e retornar o valor do imc. 
# Formula: imc = peso / altura ^ 2

# b. Faça uma função chamada "classificar_imc" que recebe o IMC e retorna uma string com a situação da pessoa baseado na tabela IMC:

# - "ABAIXO_DO_PESO"  -> Imc <= 18.5
# - "PESO_IDEAL"      -> Imc <= 25
# - "SOBREPESO"       -> Imc <= 30
# - "OBESIDADE_I"     -> imc <= 35
# - "OBESIDADE_II"    -> imc <= 40
# - "OBESIDADE_III"   -> imc > 40

def calcular_imc(peso: float, altura: float) -> float:
    imc = peso / altura ** 2
    return imc

def classificar_imc(imc: float) -> str:
    if imc <= 18.5:
        return 'ABAIXO_DO_PESO'
    elif imc <= 25:
        return 'PESO_IDEAL'
    elif imc <= 30:
        return 'SOBREPESO'
    elif imc <= 35:
        return 'OBESIDADE_I'
    elif imc <= 40:
        return 'OBESIDADE_II'
    else:
        return 'OBESIDADE_III'


peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = calcular_imc(peso, altura)
situacao = classificar_imc(imc)

# Formatar 
# print(f'O seu IMC é: {round(imc, 2)}')
print(f'O seu IMC é: {imc:.2f}')
print(f'Sitação: {situacao}')