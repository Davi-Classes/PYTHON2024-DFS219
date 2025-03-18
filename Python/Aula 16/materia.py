from db import conn


def listar_materias():
    cursor = conn.cursor()

    sql = '''
        SELECT id, nome, sigla, descricao
        FROM materias 
    '''

    cursor.execute(sql)
    dados = cursor.fetchall()
    
    cursor.close()
    return dados

def buscar_materia_pela_sigla(sigla: str):
    cursor = conn.cursor()

    sql = '''
        SELECT id, nome, sigla, descricao
        FROM materias 
        WHERE sigla = ?
    '''

    cursor.execute(sql, (sigla,))
    dado = cursor.fetchone()

    cursor.close()
    return dado

def cadastrar_materia(nome: str, sigla: str, descricao: str | None = None):
    cursor = conn.cursor()

    sql = '''
        INSERT INTO materias (nome, sigla, descricao)
        VALUES (?, ?, ?)
    '''

    cursor.execute(sql, (nome, sigla, descricao))
    
    cursor.close()
    conn.commit() # Obrigatório para Persistir os Dados

def menu():
    while True:
        print(' Gerenciar Matérias '.center(30, '='))
        print('[1] - Listar Matérias')
        print('[2] - Cadastrar Matéria')
        print('[3] - Voltar')
        print('=' * 30)

        resp = input('Selecione uma opção: ')

        if resp == '1':
            materias = listar_materias()

            for id, nome, sigla, _ in materias:
                print(f'{id} - {nome} ({sigla})')
        elif resp == '2':
            nome = input('Digite o nome da matéria: ')
            sigla = input('Digite a sigla da matéria: ')

            materia = buscar_materia_pela_sigla(sigla)

            
            if materia is not None:
                print('Já existe uma materia com essa sigla.')
                continue

            descricao = input('Descrição (Opcional): ')
            descricao = descricao if descricao.strip() != '' else None

            cadastrar_materia(nome, sigla, descricao)
            print('Materia Cadastrada com Sucesso!')
        elif resp == '3':
            break
        else:
            print('Opção Inválida!')


if __name__ == '__main__':
    menu()