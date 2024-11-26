# Função 3
# Em algumas situações, nós precisamos tratar os parametros para garantir que não aconteça um error.
def dividir(n1, n2):
    if n2 == 0:
        return None

    return n1 / n2

print(dividir(20, 5))
resultado = dividir(20, 0)

if resultado == None:
    print('Não é possivel dividir por 0')
else:
    print(resultado)