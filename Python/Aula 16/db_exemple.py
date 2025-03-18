import sqlite3


# 1. Criar uma variavel que reprensa a conexão com o banco de dados
conn = sqlite3.connect('./database.db')

# 2. Para executar consultas utilizando a conexão, nós precisamos criar um "cursor" que será aberto e fechado
cursor = conn.cursor()

sql = '''
    SELECT id, nome, sigla, descricao
    FROM materias 
'''

cursor.execute(sql)
dados = cursor.fetchall()

# Fechando o Cursor
cursor.close()

for linha in dados:
    print(linha)