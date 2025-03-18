
/*
Ex01. Crie uma nova tabela de "materias" que deve conter os campos:

- nome (Obrigatório)
- sigla (Obrigatório)
- descricao (Opcional)
*/
CREATE TABLE materias (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome VARCHAR(255) NOT NULL,
	sigla VARCHAR(5) NOT NULL,
	descricao VARCHAR(255)
);


SELECT * FROM materias;

-- Ex02. Faça um script SQL que insira 4 matérias na tabela "materias"
INSERT INTO materias (nome, sigla, descricao)
VALUES ('Matemática', 'MAT', NULL),
		('Lógica de Programação', 'LP', 'Algoritmos e estruturas básicas de lógica de programação.'),
		('HTML e CSS', 'HC', 'Introdução a desenvolvimento Web com HTML e CSS'),
		('Javascript', 'JS', NULL);

-- Ex03. Faça um script SQL que insira 5 alunos na tabela de "alunos"
INSERT INTO alunos (nome, cpf, data_nascimento)
VALUES ('Raul', '00011122233', '1997-03-14'),
		('Rafael', '00011122255', '1999-05-10'),
		('Matheus', '12234345600', '1998-04-12');