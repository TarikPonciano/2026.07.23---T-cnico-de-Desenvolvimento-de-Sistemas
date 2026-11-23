-- CAPÍTULO 4 · GABARITO DA PRÁTICA 4 · Planeje o script da oficina
-- Banco: um banco só para a oficina (ex.: oficina). Situação: Oficina Turbo, Prática 8 do Capítulo 2.
-- Pode rodar quantas vezes quiser: o script apaga e recria as tabelas.
-- Os comandos que dão erro de propósito estão comentados, com a mensagem esperada.
--
-- Nomes: o MER do slide usa telefone, placa, modelo, descricao, preco e qtd.
-- Aqui cada atributo leva o nome da tabela, como no banco da turma:
--   telefone → telefone_cliente · placa → placa_veiculo · modelo → modelo_veiculo
--   descricao → descricao_os · preco → preco_peca · qtd → qtd_item
-- O ano do veículo (ano_veiculo) vem do briefing do Capítulo 2.


-- =====================================================================
-- RESPOSTAS DO PLANEJAMENTO
-- =====================================================================

-- 1) Ordem dos CREATE TABLE: pais antes dos filhos.
--    clientes, mecanicos, pecas → não têm FK: vêm primeiro, em qualquer ordem
--    veiculos                   → aponta para clientes
--    ordens_servico             → aponta para veiculos e mecanicos
--    itens_os                   → aponta para ordens_servico e pecas
--
-- 2) Ordem dos DROP TABLE IF EXISTS: a inversa, filhos antes dos pais.
--    itens_os, ordens_servico, veiculos e, depois, pecas, mecanicos e clientes.
--
-- 3) As 5 FKs, no formato do slide (a regra na linha da coluna):
--    veiculos:       cod_cliente  integer NOT NULL CONSTRAINT fk_veic_cliente REFERENCES clientes (cod_cliente)
--    ordens_servico: cod_veiculo  integer NOT NULL CONSTRAINT fk_os_veiculo   REFERENCES veiculos (cod_veiculo)
--    ordens_servico: cod_mecanico integer NOT NULL CONSTRAINT fk_os_mecanico  REFERENCES mecanicos (cod_mecanico)
--    itens_os:       cod_os       integer NOT NULL CONSTRAINT fk_item_os      REFERENCES ordens_servico (cod_os)
--    itens_os:       cod_peca     integer NOT NULL CONSTRAINT fk_item_peca    REFERENCES pecas (cod_peca)
--    O NOT NULL torna a FK obrigatória: sem ele, a coluna aceitaria ficar vazia.
--    No script abaixo, as FKs ficam no fim da tabela (CONSTRAINT ... FOREIGN KEY ... REFERENCES).
--    As duas formas criam a mesma regra.
--
-- 4) CHECK da quantidade:
--    CONSTRAINT ck_item_qtd CHECK (qtd_item > 0)
--
-- PENSE E RESPONDA: Três tabelas não têm FK. Elas podem ser criadas em qualquer ordem entre si? Por quê?
-- Sim. clientes, mecanicos e pecas não têm REFERENCES: nenhuma precisa de outra tabela já criada.
-- A ordem só importa entre pai e filho. No DROP é igual: depois dos filhos, as três saem em qualquer ordem.


-- =====================================================================
-- 1) Apagar: filhos antes dos pais
-- =====================================================================

-- O nome no DROP tem que ser o mesmo do CREATE.
-- Erro comum: DROP de ordens_servico e CREATE de ordem_servicos. A primeira execução passa;
-- na segunda, o DROP não acha ordens_servico, a ordem_servicos continua lá, e o DROP de veiculos falha:
-- ERROR: cannot drop table veiculos because other objects depend on it
-- DETAIL: constraint fk_os_veiculo on table ordem_servicos depends on table veiculos

DROP TABLE IF EXISTS itens_os;
DROP TABLE IF EXISTS ordens_servico;
DROP TABLE IF EXISTS veiculos;
DROP TABLE IF EXISTS pecas;
DROP TABLE IF EXISTS mecanicos;
DROP TABLE IF EXISTS clientes;


-- =====================================================================
-- 2) Criar: pais antes dos filhos
-- =====================================================================

-- Todas as PKs são geradas pelo banco (GENERATED ALWAYS AS IDENTITY).
-- As regras com nome ficam no fim da tabela: é o nome que aparece no erro.

-- clientes: CPF e telefone com 11 caracteres (o telefone já com DDD).
-- Em SQL, a comparação é com um = só. Erro comum: LENGTH(cpf_cliente) == 11
-- ERROR: operator does not exist: integer == integer
-- O char(11) completa o que falta com espaços, e o LENGTH não conta os espaços do fim:
-- um CPF de 10 dígitos dá 10, e o CHECK recusa.
CREATE TABLE clientes (
  cod_cliente      integer      GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  nome_cliente     varchar(100) NOT NULL,
  cpf_cliente      char(11)     NOT NULL UNIQUE,
  telefone_cliente char(11)     NOT NULL,
  CONSTRAINT ck_cpf_tamanho CHECK (LENGTH(cpf_cliente) = 11)
);

CREATE TABLE mecanicos (
  cod_mecanico  integer      GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  nome_mecanico varchar(100) NOT NULL
);

CREATE TABLE pecas (
  cod_peca   integer       GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  nome_peca  varchar(80)   NOT NULL,
  preco_peca numeric(8, 2) NOT NULL,
  CONSTRAINT ck_preco_peca CHECK (preco_peca >= 0)
);

-- veiculos: a placa no padrão Mercosul tem 7 caracteres (ABC1D23) e não se repete.
CREATE TABLE veiculos (
  cod_veiculo    integer     GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  placa_veiculo  char(7)     NOT NULL UNIQUE,
  modelo_veiculo varchar(60) NOT NULL,
  ano_veiculo    integer     NOT NULL,
  cod_cliente    integer     NOT NULL,
  CONSTRAINT fk_veic_cliente FOREIGN KEY (cod_cliente) REFERENCES clientes (cod_cliente)
);

-- ordens_servico: a data vem do dia, se não for informada.
CREATE TABLE ordens_servico (
  cod_os       integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  data_os      date    NOT NULL DEFAULT CURRENT_DATE,
  descricao_os text    NOT NULL,
  cod_veiculo  integer NOT NULL,
  cod_mecanico integer NOT NULL,
  CONSTRAINT fk_os_veiculo  FOREIGN KEY (cod_veiculo)  REFERENCES veiculos (cod_veiculo),
  CONSTRAINT fk_os_mecanico FOREIGN KEY (cod_mecanico) REFERENCES mecanicos (cod_mecanico)
);

-- itens_os: liga a ordem à peça (o N:N do MER) e guarda a quantidade.
-- O UNIQUE do par impede a mesma peça duas vezes na mesma ordem: nesse caso, aumenta-se a quantidade.
CREATE TABLE itens_os (
  cod_item integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  qtd_item integer NOT NULL,
  cod_os   integer NOT NULL,
  cod_peca integer NOT NULL,
  CONSTRAINT fk_item_os      FOREIGN KEY (cod_os)   REFERENCES ordens_servico (cod_os),
  CONSTRAINT fk_item_peca    FOREIGN KEY (cod_peca) REFERENCES pecas (cod_peca),
  CONSTRAINT ck_item_qtd     CHECK (qtd_item > 0),
  CONSTRAINT uq_item_os_peca UNIQUE (cod_os, cod_peca)
);


-- =====================================================================
-- 3) Dados: pais antes dos filhos
-- =====================================================================

-- Sem informar os códigos: o banco gera 1, 2, 3... na ordem das linhas.
INSERT INTO clientes (nome_cliente, cpf_cliente, telefone_cliente)
VALUES ('Carlos Menezes',   '12345678901', '81991234567'),
       ('Ana Beatriz Lima', '98765432100', '81988887777');

INSERT INTO mecanicos (nome_mecanico)
VALUES ('João Batista'),
       ('Renata Souza');

INSERT INTO pecas (nome_peca, preco_peca)
VALUES ('Filtro de óleo',     45.00),
       ('Óleo 5W30 (litro)',  38.90),
       ('Pastilha de freio', 120.00);

-- O Carlos (cliente 1) tem dois carros.
INSERT INTO veiculos (placa_veiculo, modelo_veiculo, ano_veiculo, cod_cliente)
VALUES ('ABC1D23', 'Onix', 2019, 1),
       ('KLM4E56', 'HB20', 2021, 2),
       ('PQR7F89', 'Gol',  2012, 1);

INSERT INTO ordens_servico (data_os, descricao_os, cod_veiculo, cod_mecanico)
VALUES ('2026-10-20', 'Troca de óleo e filtro',       1, 1),
       ('2026-10-22', 'Troca das pastilhas de freio', 2, 2);

-- A ordem 1 usou duas peças; a ordem 2, uma.
INSERT INTO itens_os (qtd_item, cod_os, cod_peca)
VALUES (1, 1, 1),
       (4, 1, 2),
       (2, 2, 3);

SELECT * FROM ordens_servico;

-- Resultado esperado:
-- cod_os | data_os    | descricao_os                 | cod_veiculo | cod_mecanico
-- 1      | 2026-10-20 | Troca de óleo e filtro       | 1           | 1
-- 2      | 2026-10-22 | Troca das pastilhas de freio | 2           | 2

SELECT * FROM itens_os;

-- Resultado esperado:
-- cod_item | qtd_item | cod_os | cod_peca
-- 1        | 1        | 1      | 1
-- 2        | 4        | 1      | 2
-- 3        | 2        | 2      | 3


-- =====================================================================
-- 4) Conferência: as 5 FKs criadas
-- =====================================================================

-- No pgAdmin: Tables → (tabela) → Constraints. Pelo SQL, a lista das FKs e de para onde cada uma aponta:
SELECT conrelid::regclass AS tabela, conname AS regra, confrelid::regclass AS aponta_para
FROM pg_constraint
WHERE conname IN ('fk_veic_cliente', 'fk_os_veiculo', 'fk_os_mecanico', 'fk_item_os', 'fk_item_peca')
ORDER BY tabela, regra;

-- Resultado esperado: 5 linhas
-- tabela         | regra           | aponta_para
-- veiculos       | fk_veic_cliente | clientes
-- ordens_servico | fk_os_mecanico  | mecanicos
-- ordens_servico | fk_os_veiculo   | veiculos
-- itens_os       | fk_item_os      | ordens_servico
-- itens_os       | fk_item_peca    | pecas


-- =====================================================================
-- 5) Testes: cada regra recusando um dado errado
-- =====================================================================
-- Rode um teste de cada vez (selecione as linhas e F5) para ver a mensagem.
-- Com GENERATED, todo INSERT recusado gasta um número: os códigos podem pular.

-- CPF com 10 dígitos:
-- INSERT INTO clientes (nome_cliente, cpf_cliente, telefone_cliente)
-- VALUES ('Paulo Reis', '1234567890', '81977776666');
-- ERROR: new row for relation "clientes" violates check constraint "ck_cpf_tamanho"
-- DETAIL: Failing row contains (3, Paulo Reis, 1234567890 , 81977776666).
-- O espaço depois do 1234567890 é o que o char(11) completou.

-- CPF com 12 dígitos: quem recusa é o tipo char(11), antes do CHECK:
-- INSERT INTO clientes (nome_cliente, cpf_cliente, telefone_cliente)
-- VALUES ('Paulo Reis', '123456789012', '81977776666');
-- ERROR: value too long for type character(11)

-- CPF repetido (o do Carlos). O UNIQUE sem nome recebe um nome automático:
-- INSERT INTO clientes (nome_cliente, cpf_cliente, telefone_cliente)
-- VALUES ('Paulo Reis', '12345678901', '81977776666');
-- ERROR: duplicate key value violates unique constraint "clientes_cpf_cliente_key"
-- DETAIL: Key (cpf_cliente)=(12345678901) already exists.

-- Veículo de um cliente que não existe:
-- INSERT INTO veiculos (placa_veiculo, modelo_veiculo, ano_veiculo, cod_cliente)
-- VALUES ('XYZ9A87', 'Uno', 2010, 99);
-- ERROR: insert or update on table "veiculos" violates foreign key constraint "fk_veic_cliente"
-- DETAIL: Key (cod_cliente)=(99) is not present in table "clientes".

-- Ordem de serviço sem mecânico (a FK é obrigatória):
-- INSERT INTO ordens_servico (descricao_os, cod_veiculo)
-- VALUES ('Alinhamento', 3);
-- ERROR: null value in column "cod_mecanico" of relation "ordens_servico" violates not-null constraint

-- Ordem de serviço de um mecânico que não existe:
-- INSERT INTO ordens_servico (descricao_os, cod_veiculo, cod_mecanico)
-- VALUES ('Alinhamento', 3, 9);
-- ERROR: insert or update on table "ordens_servico" violates foreign key constraint "fk_os_mecanico"
-- DETAIL: Key (cod_mecanico)=(9) is not present in table "mecanicos".

-- Quantidade zero:
-- INSERT INTO itens_os (qtd_item, cod_os, cod_peca)
-- VALUES (0, 2, 1);
-- ERROR: new row for relation "itens_os" violates check constraint "ck_item_qtd"

-- Peça que não existe:
-- INSERT INTO itens_os (qtd_item, cod_os, cod_peca)
-- VALUES (1, 2, 50);
-- ERROR: insert or update on table "itens_os" violates foreign key constraint "fk_item_peca"
-- DETAIL: Key (cod_peca)=(50) is not present in table "pecas".

-- A mesma peça de novo na ordem 1 (a peça 2 já está lá):
-- INSERT INTO itens_os (qtd_item, cod_os, cod_peca)
-- VALUES (1, 1, 2);
-- ERROR: duplicate key value violates unique constraint "uq_item_os_peca"
-- DETAIL: Key (cod_os, cod_peca)=(1, 2) already exists.

-- Excluir o cliente que tem veículo (filhos antes do pai):
-- DELETE FROM clientes WHERE cod_cliente = 2;
-- ERROR: update or delete on table "clientes" violates foreign key constraint "fk_veic_cliente" on table "veiculos"
-- DETAIL: Key (cod_cliente)=(2) is still referenced from table "veiculos".
