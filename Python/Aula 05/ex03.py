nomes = []

def listar_nomes(nomes: list):
    print('Nomes: ')
    for nome in nomes:
        print(f'- {nome}')

def adicionar_nome(dados: list):
    nome = input('Digite o nome: ')
    dados.append(nome)

while True:
    print(' Armazenador de Nomes '.center(30, '-'))
    print('[1] - Listar Nomes')
    print('[2] - Adicionar novo Nome')
    print('[3] - Sair')
    print('-' * 30)

    opcao = input('Digite uma opção: ')

    if opcao == '1':
        listar_nomes(nomes)
    elif opcao == '2':
        adicionar_nome(nomes)
    elif opcao == '3':
        print('Saindo do programa...')
        break
    else:
        print('Opção Inválida. Digite Novamente.')

print('Fim do Programa.')