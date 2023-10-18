# Banco de dados - SQL

## SQL Data types
- Numéricos
- Cadeia de caracteres
- Valores temporais

### Numéricos 
**Inteiros**: bit, tinyint, smallint, int, mediumint, bigint  
**Ponto-flutuantes**: float, double
**Ponto-fixo**: decimal

### Cadeia de caracteres
**Binários**: binary, varbinary, blob (grande volume)  
**Não binários**: char, nchar, varchar, nvarchar, text

#### char x varchar
**char** ocupa todo o espaço definido
**varchar** ocupa o tamanho do texto + 1 para identificar o final

`nome char(100)`: 'Maria' ocupará 100  
`nome varchar(100)`: 'Maria' ocupará 6

#### nchar x nvarchar
Suportam UNICODE

### Temporais
**Data**: date, year
**Hora**: time
**Data e hora**: datetime, timestamp

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