-- CAPÍTULO 3 · GABARITO DA PRÁTICA 4 · Agora é com você: a biblioteca
-- Banco: biblioteca
-- Nomes como montados em aula: tabelas no singular, FK como tabela_cod
-- (editora_cod, livro_cod, leitor_cod) e atributos com o nome da tabela no fim.


-- =====================================================================
-- 1. Crie o banco biblioteca.
-- =====================================================================

-- Rode esta linha numa Query Tool aberta no banco postgres.
-- Depois, abra uma Query Tool NOVA no banco biblioteca e rode o resto do arquivo.

--CREATE DATABASE biblioteca;


-- =====================================================================
-- 2 e 3. Crie as 4 tabelas. Pelas regras, configure PK, NOT NULL, UNIQUE e DEFAULT.
-- =====================================================================

-- Como cada regra da ficha virou SQL:
--   "código; identifica"        → PRIMARY KEY
--   "obrigatório"               → NOT NULL
--   "não se repete"             → UNIQUE
--   "se não for informada, ..." → DEFAULT
-- serial = número inteiro que o banco pode gerar sozinho (1, 2, 3...).
-- IF NOT EXISTS: se a tabela já existe, o CREATE é pulado, sem erro.

-- editora: nome obrigatório; cidade opcional.
CREATE TABLE IF NOT EXISTS public.editora
(
    cod_editora serial,
    nome_editora character varying(255) NOT NULL,
    cidade_editora character varying(255),
    PRIMARY KEY (cod_editora)
);

-- leitor: o e-mail não se repete (UNIQUE).
-- Decisões da turma, além da ficha: e-mail obrigatório (NOT NULL)
-- e turma 'N/A' quando não for informada.
CREATE TABLE IF NOT EXISTS public.leitor
(
    cod_leitor serial,
    nome_leitor character varying(255) NOT NULL,
    email_leitor character varying(255) NOT NULL,
    turma_cod character varying(10) NOT NULL DEFAULT 'N/A',
    PRIMARY KEY (cod_leitor),
    UNIQUE (email_leitor)
);

-- livro: ISBN com 13 dígitos e sem repetir → char(13) + UNIQUE.
-- ISBN é texto, não número: ninguém faz conta com ele, e pode começar com zero.
-- Decisões da turma, além da ficha: ISBN obrigatório, ano 2026 e editora 1 como padrão.
-- Atenção ao DEFAULT 1: livro lançado sem editora fica com a Editora Aurora, sem aviso.
CREATE TABLE IF NOT EXISTS public.livro
(
    cod_livro serial,
    titulo_livro character varying(255) NOT NULL,
    isbn_livro character(13) NOT NULL,
    ano_livro integer NOT NULL DEFAULT 2026,
    editora_cod integer NOT NULL DEFAULT 1,
    PRIMARY KEY (cod_livro),
    UNIQUE (isbn_livro)
);

-- emprestimo:
--   data de retirada "se não for informada, é hoje" → DEFAULT CURRENT_DATE
--   devolução "vazia até a devolução"                → sem NOT NULL
--   renovações "obrigatório; começa em 0"            → NOT NULL DEFAULT 0
-- Decisão da turma: livro e leitor obrigatórios (empréstimo sempre tem os dois).
-- Sem FK (Capítulo 3), o banco ainda não confere se o livro e o leitor existem.
CREATE TABLE IF NOT EXISTS public.emprestimo
(
    cod_emprestimo serial,
    livro_cod integer NOT NULL,
    leitor_cod integer NOT NULL,
    data_retirada_emprestimo date NOT NULL DEFAULT CURRENT_DATE,
    data_devolucao_emprestimo date,
    renovacoes_emprestimo integer NOT NULL DEFAULT 0,
    PRIMARY KEY (cod_emprestimo)
);


-- =====================================================================
-- 4. Confira a aba SQL de cada tabela.
-- =====================================================================

-- O pgAdmin mostra o serial "por extenso":
--   cod_editora integer NOT NULL DEFAULT nextval('editora_cod_editora_seq'::regclass)
-- serial é um atalho para isso: inteiro, obrigatório e com um contador como DEFAULT.


-- =====================================================================
-- 5. Lance os dados do próximo slide.
-- =====================================================================

INSERT INTO public.editora (cod_editora, nome_editora, cidade_editora) VALUES
(1, 'Editora Aurora', 'Recife'),
(2, 'Editora Horizonte', 'São Paulo'),
(3, 'Editora Código', 'Recife');

INSERT INTO public.livro (cod_livro, titulo_livro, isbn_livro, ano_livro, editora_cod) VALUES
(10, 'Dom Casmurro', '9786500000101', 1899, 1),
(11, 'O Cortiço', '9786500000102', 1890, 1),
(12, 'Iracema', '9786500000103', 1865, 2),
(13, 'Lógica de Programação', '9786500000104', 2019, 3),
(14, 'Banco de Dados Essencial', '9786500000105', 2021, 3);

-- Lia Rocha: na ficha, o e-mail dela é [null]. Como aqui email_leitor é NOT NULL,
-- ela recebeu lia@email.com. Para seguir a ficha, tire o NOT NULL de email_leitor
-- e lance NULL: o UNIQUE aceita vários NULL.
INSERT INTO public.leitor (cod_leitor, nome_leitor, email_leitor, turma_cod) VALUES
(1, 'Marcos Paulo', 'marcos@email.com', 'TDS-1'),
(2, 'Júlia Reis', 'julia@email.com', 'TDS-2'),
(3, 'Lia Rocha', 'lia@email.com', 'TDS-1'),
(4, 'Rui Melo', 'rui@email.com', 'ADM-1');

-- Datas no formato do banco: 'AAAA-MM-DD'. Devolução vazia = NULL.
INSERT INTO public.emprestimo (cod_emprestimo, livro_cod, leitor_cod, data_retirada_emprestimo, data_devolucao_emprestimo, renovacoes_emprestimo) VALUES
(1, 10, 1, '2026-09-01', '2026-09-10', 0),
(2, 12, 1, '2026-09-15', NULL, 1),
(3, 11, 2, '2026-09-20', NULL, 0),
(4, 13, 4, '2026-09-22', '2026-09-30', 0),
(5, 10, 3, '2026-10-01', NULL, 0);

-- Conferência: 3 editoras, 5 livros, 4 leitores e 5 empréstimos.
SELECT
  (SELECT count(*) FROM editora)    AS editoras,
  (SELECT count(*) FROM livro)      AS livros,
  (SELECT count(*) FROM leitor)     AS leitores,
  (SELECT count(*) FROM emprestimo) AS emprestimos;

-- Atenção: os códigos foram informados à mão, e o contador do serial não fica sabendo.
-- Um INSERT sem código tenta usar o 1, que já existe (rode só esta linha para ver o erro):
-- INSERT INTO editora (nome_editora) VALUES ('Editora Nova');
-- ERROR: duplicate key value violates unique constraint "editora_pkey"
-- DETAIL: Key (cod_editora)=(1) already exists.
-- Nos exercícios, os códigos sempre vêm informados. Ver Capítulo 4: serial e GENERATED.


-- PENSE E RESPONDA: Por que emprestimo ganhou um código próprio, se já guarda o livro e o leitor?
-- Porque o par livro + leitor se repete: o mesmo leitor pode pegar o mesmo livro de novo
-- em outro mês. O par não identifica um empréstimo; o cod_emprestimo identifica.
-- E a regra da turma é PK própria em cada tabela.


-- Para recriar o banco do zero (comandos do Capítulo 4), rode antes do CREATE TABLE:
-- DROP TABLE IF EXISTS emprestimo, livro, leitor, editora;
