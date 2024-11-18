aluno = {}
notas = []

aluno['nome'] = input('Digite o nome do aluno: ')
for n in range(1, 4):
    nota = float(input(f'Digite a {n} nota: '))
    notas.append(nota)

aluno['notas'] = notas
aluno['media'] = sum(aluno['notas']) / len(aluno['notas'])
# Ternário
aluno['situacao'] = 'APROVADO' if aluno['media'] >= 6 else 'REPROVADO'

# if aluno['media'] >= 6:
#     aluno['situacao'] = 'APROVADO'
# else: 
#     aluno['situacao'] = 'REPROVADO'

print(f'Aluno: {aluno.get("nome")}')
print(f'Notas: {aluno.get("notas")}')
print(f'Média: {aluno.get("media"):.1f}')
print(f'Situação: {aluno.get("situacao")}')
