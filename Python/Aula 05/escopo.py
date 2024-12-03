# Exemplo 1 - Acessando Global
numero1 = 14 # Escopo Global

def mostrar1():
    print(numero1) # Acessar a variavel global "numero1"

mostrar1()


# Exemplo 2 - Acessando Local
numero2 = 15 # Escopo Global

def mostrar2(numero2): # Variavel de Escopo Local
    print(numero2)

mostrar2(2)

# Exemplo 3 - Alterando Local
numero3 = 15 # Escopo Global

def mostrar3(): 
    numero3 = 2 # Variavel de Escopo Local
    print(numero3) # Variavel de Escopo Local

mostrar3()
print(numero3) # Variavel de Escopo Global