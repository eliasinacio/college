# Banco de dados - SQL

## SQL Data types

- Numéricos
- Cadeia de caracteres
- Valores temporais

### Numéricos

- Inteiros - bit, tinyint, smallint, int, mediumint, bigint
- Ponto-flutuantes - float, double
- Ponto-fixo - decimal

### Cadeia de caracteres

- Binários - binary, varbinary, blob (grande volume)
- Não binários - char, nchar, varchar, nvarchar, text

#### char x varchar

char ocupa todo o espaço definido
varchar ocupa o tamanho do texto + 1 para identificar o final

nome char(100) -> 'Maria' ocupará 100
nome varchar(100) -> 'Maria' ocupará 6

#### nchar x nvarchar

Suportam UNICODE

### Temporais

Data - date, year
Hora - time
Data e hora - datetime, timestamp

## SQL Commands

Mostrar bancos de dados:

```SQL
show databases;
```

Criar novo banco de dados:

```SQL
create database banco;
```

Usar determinado banco de dados criado:

```SQL
use banco;
```

Mostrar o banco de dados que está sendo usado:

```SQL
select database();
```

Criar tabela no banco:

```SQL
create table tabela (
    id int,
    nome varchar(100)
);
```

Inserir dado na tabela:

```SQL
insert into tabela;
```

Mostrar tipos e especificações da tabela:

```SQL
describe tabela;
```

## SQL PK, FK e UK

Declarar chaves primária (PK), estrangeira (FK) e Unique Key (UK).

### Primary key

Diferencia uma linha da outra na tabela, não permite duplicados.

```SQL
create table cidade (
    id int primary key, -- define campo id como chave promária
    nome varchar(100)
);
```

### Unique key

Também não permite que seja repetido o mesmo valor em linhas diferentes da tabela.

```SQL
create table cidade (
    id int primary key,
    nome varchar(100),
    sigla char(03) unique -- define sigla como unique key
);
```

### Foreign key

Define que o valor do campo deve existir/coincidir em outra tabela, referenciada no `constraint`.

```SQL
create table cliente (
    id int primary key,
    nome varchar(100),
    idCidade int,
    constraint fkClienteCidade foreign key (idCidade) references cidade(id)
);
```

## SQL Constraints

Restringe, limita e/ou padroniza em nível de coluna ou tabela.

```SQL
create table aluno (
id int primary key,
    nome varchar(100) not null, -- valor não pode ser nulo
    genero char(01),
    estadoCivil char(01) check (estadoCivil in ('S', 'C', 'V')), -- valor deve ser 'S', 'C' ou 'V'
    renda decimal(10,2) default 0 -- valor será 0 caso não seja definido
);
```

## SQL Alterações e Auto Increment

```SQL
create table cidades (
    id int primary key auto_increment, -- ao inserir uma nova linha, não precisa especificar, será incrementado
    nome varchar(100) not null,
    cepGeral int unsigned zerofill
    -- unsigned: maior que 0
    -- zerofill: preenche com 0 à esquerda
);
```

Adicionar um novo campo à tabela:

```SQL
alter table cidades add dddd char(05);
```

Alterar o nome do campo:

```SQL
alter table cidades change dddd ddd char (05);
```

Alterar uma propriedade do campo:

```SQL
alter table cidades modify ddd char (03);
```

Remover campo:

```SQL
alter table cidades drop cepGeral;
```

## SQL - INSERT

Insert completo:

```SQL
insert into aluno (id, nome, genero, estadoCivil, renda) values (1, 'Elias', 'M', 'S', 3500);
```

Insert especificando apenas os valores:

```SQL
insert into aluno values (2, 'Maria', 'F', 'S', 4500); -- precisa estar na ordem da tabela
```

Insert de parte dos campos:

```SQL
insert into aluno (id, nome) values (3, 'Bárbara'); -- não pode faltar campos obrigatórios ou com constraints
```

Insert de várias linhas:

```SQL
insert into aluno (id, nome, genero) values (5, 'Élison', 'M'), (6, 'Ana', 'F'), (7, 'Rafa', 'F');
```

Insert de outra tabela:

```SQL
insert into turma (id, nome, genero)
    select id, nome, genero from aluno
```

## SQL - DELETE e UPDATE

Alterar o valor de um campo:

```SQL
update aluno set nome = 'Julia' where id = 6;
```

Deletar uma linha da tabela:

```SQL
delete from aluno where id = 3;
```

## SQL - SELECT

Select com filtros:

```SQL
select * from aluno where genero = 'F';
```

```SQL
select * from aluno where genero = 'F' and renda >= 4500;
```

```SQL
select * from aluno where genero in ('F', 'M');
```

Select com ordenação:

```SQL
select nome from aluno order by nome asc; -- asc / desc
```

## SQL - JOIN

### INNER JOIN

Traz o que houver em comum entre as colunas:

```SQL
/* Definidas as tabelas */
create table cidade (
    id int primary key auto_increment,
    nomeCidade varchar(100),
    estado char(2)
);

create table estado (
    id int auto_increment,
    nomeEstado varchar(100),
    sigla char(2),
    constraint pkEstado primary key (id)
);

/* Adicionados dados */
insert into cidade values (1, 'Juazeiro do Norte', 'CE');
insert into cidade values (2, 'Crato', 'CE');
insert into cidade values (3, 'Barbalha', 'CE');
insert into cidade values (4, 'São Paulo', 'SP');
insert into cidade values (5, 'Taubaté', 'SP');
insert into cidade values (6, 'Rio de Janeiro', 'RJ');

insert into estado values (1, 'Ceará', 'CE');
insert into estado values (2, 'São Paulo', 'SP');
insert into estado values (3, 'Paraná', 'PR');
insert into estado values (4, 'Rio de Janeiro', 'RJ');

/* Traz os nomes das cidades e estados, em que estão associadas a cidade ao estado */
select nomeCidade, nomeEstado from cidade inner join estado on cidade.estado = estado.sigla;

/* Cidades que não tem estado ou estados que não têm cidades não são retornados */
```

Saída:

| nomeCidade        | nomeEstado     |
| ----------------- | -------------- |
| Juazeiro do Norte | Ceará          |
| Crato             | Ceará          |
| Barbalha          | Ceará          |
| São Paulo         | São Paulo      |
| Taubaté           | São Paulo      |
| Rio de Janeiro    | Rio de Janeiro |

### Cross Join

Cruza os dados, multiplica as linhas de uma tabela pelas linhas da outra:

```SQL
select nomeCidade, nomeEstado
from cidade, estado
order by nomeCidade

/* Output traria todas as cidades repetidamente para cada estado */
```

### LEFT JOIN / RIGHT JOIN

Traz todas as linhas da tabela à esquerda/direita e preenche com as associações caso exista:

```SQL
select nomeCidade, nomeEstado 
from cidade 
left join estado 
on cidade.estado = estado.sigla;
```

Saída:

| nomeCidade         | nomeEstado     |
| ------------------ | -------------- |
| Juazeiro do Norte  | Ceará          |
| Crato              | Ceará          |
| Barbalha           | Ceará          |
| São Paulo          | São Paulo      |
| Taubaté            | São Paulo      |
| Rio de Janeiro     | Rio de Janeiro |
| Balneário Camboriú | `null`         |

### Self Join

Seleciona os dados cruzando a tabela com ela mesma.

Por exemplo quando temos uma tabela de funcionários, em que existe o campo gerente com o Id de outro funcionário:

```SQL
select funcionario.nome, gerente.nome
from funcionario
inner join funcionario gerente
on funcionario.gerente = gerente.id
```

Trará a lista com os funncionários que possuem gerente */
Caso fosse feito left join, traria todos os funcionários na primeira coluna e preencheria a coluna gerente caso existisse gerente para esse funcionário.

### Full Join

Traria todas as linhas de uma tabela e todos as linhas da outra tabela.

## SQL Outros comandos

### Alias - Apelido

**As**: apelida algo:

```SQL
select nomeFunc as 'Nome do funcionário' from funcionario
```

Mostrará no Output 'Nome do funcionário' como nome da coluna.

```SQL
select nome from cidade c
where c.uf = 'CE';
```

A partir da declaração cidade tem o apelido de c dentro da query.

### Limit

Limita a saída ao tamanho especificado:

```SQL
select * from funcionario limit 3; -- Trará apenas 3 linhas
```

### Union

Une dois selects numa mesma saída:

```SQL
select nomeFunc from funcionario
union -- Para trazer todos os casos, mesmo repetidos, usar `union all`
select nomeCliente from cliente

/* Trará os nomes de todos os funcionários e clientes numa mesma coluna */
```

### Case

Faz um teste/condição:

```SQL
select nomeFunc
case
    when genero = 'F' then 'Feminino'
    when genero = 'M' then 'Masculino'
end
from funcionario;

/* Trará os funcionários e o genero, mas mostrando 'Feminino'/'Masculino' no lugar do real valor da tabela que é 'F'/'M' */
```

## SQL Subqueries

### Subconsulta

Uma query dentro de uma query

```SQL
select * from cidade 
where uf = (
    select sigla from estado
    where nome = 'Ceará'
);
```

### EXISTS

```SQL
select nome, salario from cliente 
where salario < 7000 
and exists (
    select * from cliente where salario > 11000
);
```
