CREATE DATABASE IF NOT EXISTS biblioteca;

CREATE TABLE IF NOT EXISTS public.editora
(
    cod_editora serial,
    nome_editora character varying(255) NOT NULL,
    cidade_editora character varying(255),
    PRIMARY KEY (cod_editora)
);

CREATE TABLE IF NOT EXISTS public.leitor
(
    cod_leitor serial,
    nome_leitor character varying(255) NOT NULL,
    email_leitor character varying(255) NOT NULL,
    turma_cod character varying(10) NOT NULL DEFAULT 'N/A',
    PRIMARY KEY (cod_leitor),
    UNIQUE (email_leitor)
);

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

INSERT INTO public.leitor (cod_leitor, nome_leitor, email_leitor, turma_cod) VALUES
(1, 'Marcos Paulo', 'marcos@email.com', 'TDS-1'),
(2, 'Júlia Reis', 'julia@email.com', 'TDS-2'),
(3, 'Lia Rocha', 'lia@email.com', 'TDS-1'), -- Alerta: O script diz NOT NULL, mas a imagem mostra [null]
(4, 'Rui Melo', 'rui@email.com', 'ADM-1');

INSERT INTO public.emprestimo (cod_emprestimo, livro_cod, leitor_cod, data_retirada_emprestimo, data_devolucao_emprestimo, renovacoes_emprestimo) VALUES
(1, 10, 1, '2026-09-01', '2026-09-10', 0),
(2, 12, 1, '2026-09-15', NULL, 1),
(3, 11, 2, '2026-09-20', NULL, 0),
(4, 13, 4, '2026-09-22', '2026-09-30', 0),
(5, 10, 3, '2026-10-01', NULL, 0);