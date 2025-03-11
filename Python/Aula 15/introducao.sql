-- DDL (Data Definition Language)

-- CREATE DATABASE <meu_banco>;
-- USE <meu_banco>;

-- Criando Tabela
CREATE TABLE alunos (
-- <coluna> <tipo> <caracteristicas...>
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR(255) NOT NULL,
	cpf VARCHAR(11) NOT NULL UNIQUE,
	data_nascimento DATE NOT NULL,
	observacao VARCHAR(255),
	ativo INT NOT NULL DEFAULT 1
);

-- Excluindo Tabelas
-- DROP TABLE alunos;

CREATE TABLE professores (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR(255) NOT NULL,
	registro VARCHAR(5) NOT NULL UNIQUE,
	data_nascimento DATE NOT NULL,
	sobre VARCHAR(255)
);

-----------------------
-- DQL (Data Query Language)

-- O "*" busca todas as colunas
SELECT * FROM alunos;

-- Mas também podemos especificar quais colunas queremos
SELECT * FROM professores;

----------------------------
-- DML (Data Manipulation Language)

-- Inserindo Dados
INSERT INTO professores (nome, registro, data_nascimento, sobre)
VALUES ('Davi', '00000000011', '2004-01-14', 'Desenvolvedor Backend e Professor de Full Stack'),
		('Oshiro', '00000000012', '1990-02-19', NULL);

INSERT INTO professores (nome, registro, data_nascimento)
VALUES ('Carlos', '12354', '1980-05-23');

-- Atualizando dados
UPDATE professores
SET nome = 'Davi Lucciola'
WHERE registro = '00000000011';

-- Excluindo Dados
DELETE FROM alunos
WHERE registro = '12354'; -- Muito importante a clausula WHERE




