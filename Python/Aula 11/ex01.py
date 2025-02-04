class Celular:
    # Metódo Construtor
    def __init__(self, marca: str, modelo: str, cor: str):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ligado = False
    
    def ligar(self):
        self.ligado = True
    
    def desligar(self):
        self.ligado = False

    
# a.
samsung_a55 = Celular('Samsung', 'A55', 'Azul Marinho')

# b.
print(samsung_a55.marca)

# c. 
iphone = Celular('Apple', 'Iphone 15', 'Branco')

# d.
print(iphone.modelo)
print(iphone.cor)


##############
# Ligando A55
# print(samsung_a55.ligado)
# samsung_a55.ligar()
# print(samsung_a55.ligado)

# Ligando Iphone
# print(iphone.ligado)
# iphone.ligar()
# print(iphone.ligado)
# iphone.desligar()
# print(iphone.ligado)