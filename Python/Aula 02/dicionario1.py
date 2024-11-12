# Dicionarios
# Os items tem ordem
aluno = {
    # Chave  :  Valor
    'matricula': '21343', # Item
    'nome': 'Lucas',
    'curso': 'DFS',
    'notas': [5.6, 9.5, 8.6]
}

print(aluno)

# Acessando Valores
print(aluno['matricula']) # '21343'
print(aluno.get('nome')) # 'Lucas'
print(aluno.get('nao_existe')) # None
print(aluno.get('nao_existe', 'Chave não encontrada')) # 'Chave não encontrada'

# Criando/Atualizando Chaves
aluno['matricula'] = input('Digite a nova matricula: ')
aluno['media'] = sum(aluno.get('notas')) / len(aluno.get('notas'))

dados_novos = {
    'nome': 'Lucas Souza', 
    'situacao': 'APROVADO'
}
aluno.update(dados_novos)

# Removendo Chaves

# Verifica se a chave existe no dicionário.
if 'situacao' in aluno:
    aluno.pop('situacao')