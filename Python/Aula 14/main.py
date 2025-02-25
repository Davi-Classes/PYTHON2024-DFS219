import os
from tabulate import tabulate
from endereco import Endereco
from datetime import datetime, date
from pessoa import Pessoa, PessoaRepository


# CRUD
# Create Read Update Delete
FILLCHAR = '='
LINE_WIDTH = 30


def print_line():
    print(FILLCHAR * LINE_WIDTH)


pessoa_repository = PessoaRepository([])


while True:
    os.system('clear')

    print_line()
    print(' Gerenciamento de Pessoas '.center(LINE_WIDTH))
    print_line()
    print('[1] - Listar')
    print('[2] - Detalhar (pelo CPF)')
    print('[3] - Cadastrar')
    print('[4] - Editar')
    print('[5] - Excluir')
    print('[6] - Sair')
    print_line()

    opcao = input('Selecione uma Opção: ')

    if opcao == '1':
        dados = []
        colunas = ['Nome', 'Cpf', 'Data de Nascimento']
        pessoas = pessoa_repository.buscar_todos()

        if len(pessoas) == 0:
            print('Não há pessoas cadastradas')
            print_line()
            input('Aperte <ENTER> para continuar...')
            continue

        for pessoa in pessoas:
            dados.append((pessoa.nome, pessoa.cpf, pessoa.data_nascimento))

        table = tabulate(dados, headers=colunas)
        table_width = len(table.split('\n')[1])
        print('-' * table_width)
        print(table)
        print('-' * table_width)
    elif opcao == '2':
        # 1. Pedir o CPF
        # 2. Buscar a pessoa pelo CPF
        # 3. Se encontrar a pessoa, mostra os seus dados completos (com endereço)
        # Se não encontrar a pessoa, mostra uma mensagem para o usuário
        print('Detalhando Pessoa...')
    elif opcao == '3':
        print(' Dados Pessoais '.center(LINE_WIDTH, FILLCHAR))
        nome = input('Digite o nome: ')
        cpf = input('Digite o cpf: ')

        pessoa = pessoa_repository.buscar_pelo_cpf(cpf)

        if pessoa != None:
            print('Pessoa já está cadastrada.')
            print_line()
            input('Aperte <ENTER> para continuar...')
            continue

        data_nascimento = input('Digite a data de nascimento (dd/MM/yyyy): ')
        data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
        
        print(' Dados Endereço '.center(LINE_WIDTH, FILLCHAR))
        cep = input('Digite o cep: ')
        rua = input('Digite a rua: ')
        numero = input('Digite o numero: ')
        bairro = input('Digite o bairro: ')
        cidade = input('Digite a cidade: ')
        estado = input('Digite o estado: ')
        complemento = input('Digite o complemento: ')

        endereco = Endereco(cep, rua, numero, bairro, cidade, estado, complemento)
        pessoa = Pessoa(nome, cpf, data_nascimento, endereco)

        pessoa_repository.adicionar(pessoa)

        print('Pessoa cadastrada com sucesso.')
    elif opcao == '4':
        cpf = input('Digite o CPF: ')
        pessoa = pessoa_repository.buscar_pelo_cpf(cpf)

        if pessoa == None:
            print('Pessoa não encontrada.')
            print_line()
            input('Aperte <ENTER> para continuar...')
            continue
        
        print(' Dados Pessoais '.center(LINE_WIDTH, FILLCHAR))
        nome = input('Digite o nome: ')
        data_nascimento = input('Digite a data de nascimento (dd/MM/yyyy): ')
        data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()

        print(' Dados Endereço '.center(LINE_WIDTH, FILLCHAR))
        cep = input('Digite o cep: ')
        rua = input('Digite a rua: ')
        numero = input('Digite o numero: ')
        bairro = input('Digite o bairro: ')
        cidade = input('Digite a cidade: ')
        estado = input('Digite o estado: ')
        complemento = input('Digite o complemento: ')

        endereco = Endereco(cep, rua, numero, bairro, cidade, estado, complemento)

        pessoa.nome = nome
        pessoa.data_nascimento = data_nascimento
        pessoa.endereco = endereco

    elif opcao == '5':
        cpf = input('Digite o CPF: ')
        pessoa = pessoa_repository.buscar_pelo_cpf(cpf)

        if pessoa == None:
            print('Pessoa não encontrada.')
            print_line()
            input('Aperte <ENTER> para continuar...')
            continue

        pessoa_repository.excluir_pelo_cpf(cpf)
        print('Pessoa excluida com sucesso.')
    elif opcao == '6':
        break
    else:
        print('OPÇÃO INVÁLIDA! Tente Novamente!')
    
    print_line()
    input('Aperte <ENTER> para continuar...')

print('Fim do Programa! Volte Sempre!')
