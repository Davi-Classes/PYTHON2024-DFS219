notas = []
aluno = input('Digite o nome do aluno: ')

for n in range(3):
    nota = float(input(f'Digite a {n+1}ª nota: '))
    notas.append(nota)

media = sum(notas) / len(notas)