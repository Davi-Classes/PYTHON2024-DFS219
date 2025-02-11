# Excessões
# São erros que acontecem em tempo de execução

# Try Except
# Ele tentará executar o Try
try:
    positivo = float(input('Digite um numero positivo: '))

    if positivo <= 0:
        raise Exception('Somente valores positivos são permitidos.')

    print('Valor Válido!')
# Caso aconteça um erro esperado, o except irá capturar esse erro
except Exception as err:
    print(err)
# O Finally sempre será executado.
finally:
    print('Fim do Programa!')