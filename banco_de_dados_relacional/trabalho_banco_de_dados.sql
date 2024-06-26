create table Aluno (
	idAluno int primary key,
    matricula varchar(10) not null,
    nome varchar (50) not null
);

create table Disciplina (
	idDisciplina int primary key,
    nome varchar (50) not null,
    cargaHoraria int not null
);

create table Historico (
	idAluno int,
    idDisciplina int,
	nota float not null,
    dataHistorico date not null,
	constraint fkHistoricoAluno foreign key (idAluno) references aluno(idAluno),
	constraint fkHistoricoDisciplina foreign key (idDisciplina) references disciplina(idDisciplina)
);

create table Curso (
	idCurso int primary key,
    nome varchar(50) not null
);

create table AlunoCurso (
	idAluno int,
    idCurso int,
    anoEntrada int not null,
	constraint fkAlunoAluno foreign key (idAluno) references aluno(idAluno),
	constraint fkAlunoCurso foreign key (idCurso) references curso(idCurso)
);

create table Grade (
	idGrade int primary key,
    idCurso int,
    ano int not null,
    cargaHorariaTotal int not null,
	constraint fkGradeCurso foreign key (idCurso) references curso(idCurso)
);

create table GradeDisciplina (
	idGrade int,
    idDisciplina int,
    constraint fkGradeGrade foreign key (idGrade) references grade(idGrade),
    constraint fkGradeDisciplina foreign key (idDisciplina) references disciplina(idDisciplina)
);


insert into Aluno (idAluno, matricula, nome) values
	( 1, 'ADS001', 'Alice de Souza'),
	( 2, 'BDS001', 'Ana Luiza de Paula'),
	( 3, 'CDS001', 'Maria Helena Mantovani'),
	( 4, 'DSM001', 'Marta da Silva'),
	( 5, 'ENC001', 'Viviane Chaves Filha'),
	( 6, 'ENS001', 'Paula Roberta Vitorino'),
	( 7, 'GTI001', 'Miriam Miranda'),
	( 8, 'JDS001', 'Beatriz Leopoldina'),
	( 9, 'RCS001', 'Nicole Amanda de Jesus'),
	(10, 'RCS002', 'Vitor Martins'),
	(11, 'JDS002', 'João Augusto de Moura'),
	(12, 'GTI002', 'Matheus Murilo de Souza'),
	(13, 'ENS002', 'Mario Vicente'),
	(14, 'ENC002', 'Antônio Cozer'),
	(15, 'DSM002', 'Luciano Tucolo'),
	(16, 'CDS002', 'Guilherme Koeriche'),
	(17, 'BDS002', 'Lucas Cochuelo'),
	(18, 'ADS002', 'Diogo Furlan'),
	(19, 'ADS003', 'Marcelo Luis dos Santos');

insert into Disciplina (idDisciplina, nome, cargaHoraria) values
	( 1, 'Análise de Sistemas', 60),
	( 2, 'Arquitetura de Computadores', 60),
	( 3, 'Atividade Extensionista I', 40),
	( 4, 'Atividade Extensionista II', 40),
	( 5, 'Banco de Dados', 60),
	( 6, 'Empreendedorismo', 40),
	( 7, 'Engenharia de Software', 60),
	( 8, 'Fundamentos de Sistemas de Informação', 60),
	( 9, 'Gestão de Projetos de Software', 60),
	(10, 'Lógica de Programação e Algoritmos', 80),
	(11, 'Matemática Computacional', 40),
	(12, 'Programação de Computadores', 80),
	(13, 'Programação Orientada a Objetos', 80),
	(14, 'Sistema Gerenciador de Banco de Dados', 60),
	(15, 'Sistemas Operacionais', 60);
                            
insert into Curso (idCurso, nome) values
	(1, 'Análise e Desenvolvimento de Sistemas'),
	(2, 'Banco de Dados'),
	(3, 'Ciência de Dados'),
	(4, 'Desenvolvimento Mobile'),
	(5, 'Engenharia da Computação'),
	(6, 'Engenharia de Software'),
	(7, 'Gestão da Tecnologia da Informação'),
	(8, 'Jogos Digitais'),
	(9, 'Redes de Computadores');
                         
insert into Historico (idAluno, idDisciplina, nota, dataHistorico) values
	( 3,  1, 90, '2022-12-09'),
	( 3,  3, 75, '2022-12-09'),
	( 3,  5, 85, '2022-12-09'),
	( 9,  1, 80, '2022-12-16'),
	( 9,  9, 75, '2022-12-16'),
	( 9, 11, 70, '2022-12-16'),
	(13, 12, 70, '2022-12-09'),
	(13, 13, 70, '2022-12-09'),
	(13, 14, 82, '2022-12-09'),
	(15,  2, 76, '2022-12-16'),
	(15,  4, 80, '2022-12-16'),
	(15,  6, 89, '2022-12-16');

insert into AlunoCurso (idAluno, idCurso, anoEntrada) values
	( 1, 1, 2023),
	( 2, 2, 2023),
	( 3, 3, 2022),
	( 4, 4, 2023),
	( 5, 5, 2023),
	( 6, 6, 2023),
	( 7, 7, 2023),
	( 8, 8, 2023),
	( 9, 9, 2022),
	(10, 9, 2023),
	(11, 8, 2023),
	(12, 7, 2023),
	(13, 6, 2022),
	(14, 5, 2023),
	(15, 4, 2022),
	(16, 3, 2023),
	(17, 2, 2023),
	(18, 1, 2023),
	(19, 1, 2023);

insert into Grade (idGrade, idCurso, ano, cargaHorariaTotal) values
	( 1, 1, 2021, 880),
	( 2, 2, 2022, 880),
	( 3, 3, 2022, 880),
	( 4, 4, 2022, 880),
	( 5, 5, 2019, 880),
	( 6, 6, 2022, 880),
	( 7, 7, 2022, 880),
	( 8, 8, 2022, 880),
	( 9, 9, 2019, 880),
	(10, 1, 2023, 880),
	(11, 5, 2023, 880),
	(12, 9, 2023, 880);

insert into GradeDisciplina (idGrade, idDisciplina) values
	( 1, 1), ( 1, 2), ( 1, 3), ( 1, 4), ( 1, 5), ( 1, 6), ( 1, 7), ( 1, 8), ( 1, 9), ( 1, 10), ( 1, 11), ( 1, 12), ( 1, 13), ( 1, 14), ( 1, 15),
	( 2, 1), ( 2, 2), ( 2, 3), ( 2, 4), ( 2, 5), ( 2, 6), ( 2, 7), ( 2, 8), ( 2, 9), ( 2, 10), ( 2, 11), ( 2, 12), ( 2, 13), ( 2, 14), ( 2, 15),
	( 3, 1), ( 3, 2), ( 3, 3), ( 3, 4), ( 3, 5), ( 3, 6), ( 3, 7), ( 3, 8), ( 3, 9), ( 3, 10), ( 3, 11), ( 3, 12), ( 3, 13), ( 3, 14), ( 3, 15),
	( 4, 1), ( 4, 2), ( 4, 3), ( 4, 4), ( 4, 5), ( 4, 6), ( 4, 7), ( 4, 8), ( 4, 9), ( 4, 10), ( 4, 11), ( 4, 12), ( 4, 13), ( 4, 14), ( 4, 15),
	( 5, 1), ( 5, 2), ( 5, 3), ( 5, 4), ( 5, 5), ( 5, 6), ( 5, 7), ( 5, 8), ( 5, 9), ( 5, 10), ( 5, 11), ( 5, 12), ( 5, 13), ( 5, 14), ( 5, 15),
	( 6, 1), ( 6, 2), ( 6, 3), ( 6, 4), ( 6, 5), ( 6, 6), ( 6, 7), ( 6, 8), ( 6, 9), ( 6, 10), ( 6, 11), ( 6, 12), ( 6, 13), ( 6, 14), ( 6, 15),
	( 7, 1), ( 7, 2), ( 7, 3), ( 7, 4), ( 7, 5), ( 7, 6), ( 7, 7), ( 7, 8), ( 7, 9), ( 7, 10), ( 7, 11), ( 7, 12), ( 7, 13), ( 7, 14), ( 7, 15),
	( 8, 1), ( 8, 2), ( 8, 3), ( 8, 4), ( 8, 5), ( 8, 6), ( 8, 7), ( 8, 8), ( 8, 9), ( 8, 10), ( 8, 11), ( 8, 12), ( 8, 13), ( 8, 14), ( 8, 15),
	( 9, 1), ( 9, 2), ( 9, 3), ( 9, 4), ( 9, 5), ( 9, 6), ( 9, 7), ( 9, 8), ( 9, 9), ( 9, 10), ( 9, 11), ( 9, 12), ( 9, 13), ( 9, 14), ( 9, 15),
	(10, 1), (10, 2), (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13), (10, 14), (10, 15),
	(11, 1), (11, 2), (11, 3), (11, 4), (11, 5), (11, 6), (11, 7), (11, 8), (11, 9), (11, 10), (11, 11), (11, 12), (11, 13), (11, 14), (11, 15),
	(12, 1), (12, 2), (12, 3), (12, 4), (12, 5), (12, 6), (12, 7), (12, 8), (12, 9), (12, 10), (12, 11), (12, 12), (12, 13), (12, 14), (12, 15);


	-- Questões

select Curso.nome nomeCurso, Aluno.nome nomeAluno from Curso
left join AlunoCurso on Curso.idCurso = AlunoCurso.idCurso
left join Aluno on AlunoCurso.idAluno = Aluno.idAluno
order by Curso.nome desc;

show tables;

select * from Disciplina;
select * from Historico;

select Disciplina.nome 'Disciplina', avg(Historico.nota) 'Média' from Disciplina
join Historico on Disciplina.idDisciplina = Historico.idDisciplina
group by Disciplina.nome;

select Curso.nome 'Cursos', 'Alunos' from Curso
join AlunoCurso on Aluno.idAluno = AlunoCurso.idAluno
group by Aluno.nome;

select Curso.nome Cursos, count(*) Alunos from Curso
left join AlunoCurso on Curso.idCurso = AlunoCurso.idCurso
left join Aluno on AlunoCurso.idAluno = Aluno.idAluno
group by Curso.nome;