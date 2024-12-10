def calcular_media(n1: float, n2: float, n3: float):
    """Recebe 3 valores e retorna a média entre eles.

    Args:
        n1 (float): 1º Valor
        n2 (float): 2º Valor
        n3 (float): 3º Valor

    Returns:
        float: Média dos valores
    """    
    media = (n1 + n2 + n3) / 3
    return media


media = calcular_media(4, 5, 6)
print(media)