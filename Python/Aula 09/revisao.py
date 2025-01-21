# Funções
def pesquisar(dados: list[str], pesquisa: str):
    resultado = []
    
    for dado in dados:
        if pesquisa.lower() in dado.lower():
            resultado.append(dado)

    return resultado


nomes = ['Rafael', 'Lucas', 'Raul', 'Wesley']
pesquisa = input('Digite uma pesquisa: ')

nomes_filtrados1 = pesquisar(nomes, pesquisa)
nomes_filtrados2 = pesquisar(nomes, 'lu')

print(nomes_filtrados1)
print(nomes_filtrados2)