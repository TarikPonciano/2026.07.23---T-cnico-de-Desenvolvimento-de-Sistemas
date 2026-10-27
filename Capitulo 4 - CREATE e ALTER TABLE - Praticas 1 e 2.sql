-- CAPÍTULO 4 · GABARITO DAS PRÁTICAS 1 E 2
-- Banco: escola (abra a Query Tool no banco escola, não no postgres)
-- Os comandos que dão erro de propósito estão comentados, com a mensagem esperada:
-- assim o arquivo roda inteiro, de cima a baixo.


-- =====================================================================
-- PRÁTICA 1 · Escreva o CREATE TABLE
-- =====================================================================

-- A escola quer cadastrar os eventos do semestre.
-- cod_evento          código; identifica o evento
-- titulo              texto até 80; obrigatório
-- data_evento         data; obrigatória
-- local_evento        texto até 60
-- vagas               número inteiro; obrigatório; se não informar, 30
-- inscricoes_abertas  verdadeiro ou falso; obrigatório; começa verdadeiro

CREATE TABLE eventos (
  cod_evento         integer     PRIMARY KEY,
  titulo             varchar(80) NOT NULL,
  data_evento        date        NOT NULL,
  local_evento       varchar(60),
  vagas              integer     NOT NULL DEFAULT 30,
  inscricoes_abertas boolean     NOT NULL DEFAULT true
);

-- 1. Refresh em Tables e confira a aba SQL: bate com o que você escreveu?
-- Bate. O pgAdmin só escreve de outro jeito:
--   varchar(80)  vira  character varying(80)
--   a PK vai para o fim: CONSTRAINT eventos_pkey PRIMARY KEY (cod_evento)
--   cod_evento aparece com NOT NULL (toda PK já é obrigatória)

-- 2. Insira o evento 1: Feira de Tecnologia, 20/11/2026, no Pátio.
-- Data no formato do banco: 'AAAA-MM-DD'.

INSERT INTO eventos (cod_evento, titulo, data_evento, local_evento)
VALUES (1, 'Feira de Tecnologia', '2026-11-20', 'Pátio');

-- 3. Insira o evento 2: Palestra: carreira em dados, 25/11/2026
-- — sem local, sem vagas, sem informar inscrições.

INSERT INTO eventos (cod_evento, titulo, data_evento)
VALUES (2, 'Palestra: carreira em dados', '2026-11-25');

-- 4. SELECT * FROM eventos;

SELECT * FROM eventos;

-- Resultado esperado:
-- cod_evento | titulo                      | data_evento | local_evento | vagas | inscricoes_abertas
-- 1          | Feira de Tecnologia         | 2026-11-20  | Pátio        | 30    | true
-- 2          | Palestra: carreira em dados | 2026-11-25  | [null]       | 30    | true

-- PENSE E RESPONDA: No evento 2, de onde vieram as vagas e o valor de inscricoes_abertas?
-- Dos DEFAULTs: a coluna omitida no INSERT recebe o valor padrão (30 e true).
-- local_evento não tem DEFAULT nem NOT NULL, então ficou vazia (NULL).


-- =====================================================================
-- PRÁTICA 2 · Os eventos mudaram de ideia
-- =====================================================================

-- 1. Guardar o nome do responsável pelo evento (texto até 100).

ALTER TABLE eventos ADD COLUMN responsavel varchar(100);

-- Os dois eventos já cadastrados ficam com responsavel vazio (NULL).

-- 2. Alguns títulos são longos: o título passa a aceitar 150 caracteres.

ALTER TABLE eventos ALTER COLUMN titulo TYPE varchar(150);

-- 3. A coluna local_evento passa a se chamar sala.

ALTER TABLE eventos RENAME COLUMN local_evento TO sala;

-- 4. Eventos novos começam com 40 vagas.

ALTER TABLE eventos ALTER COLUMN vagas SET DEFAULT 40;

-- Só vale para os próximos INSERTs: os eventos 1 e 2 continuam com 30.

-- 5. Guardar o horário, obrigatório, tipo time.
-- Tente primeiro sem DEFAULT. O que aconteceu? Resolva com padrão '19:00'.

-- Primeira tentativa (rode só esta linha para ver o erro):
-- ALTER TABLE eventos ADD COLUMN horario time NOT NULL;
-- ERROR: column "horario" of relation "eventos" contains null values
--
-- A tabela já tem 2 linhas. A coluna nova nasceria vazia nelas, e o NOT NULL recusa.
-- Com DEFAULT, as linhas que já existem recebem 19:00 e a regra é cumprida.

ALTER TABLE eventos ADD COLUMN horario time NOT NULL DEFAULT '19:00';

-- 6. Desistiram do responsável: apague essa coluna.

ALTER TABLE eventos DROP COLUMN responsavel;

-- 7. A tabela passa a se chamar eventos_escola.
-- Insira o evento 3, Hackathon, 05/12/2026, e confira com SELECT.

ALTER TABLE eventos RENAME TO eventos_escola;

INSERT INTO eventos_escola (cod_evento, titulo, data_evento)
VALUES (3, 'Hackathon', '2026-12-05');

SELECT * FROM eventos_escola;

-- Resultado esperado (horario entrou no fim da tabela):
-- cod_evento | titulo                      | data_evento | sala   | vagas | inscricoes_abertas | horario
-- 1          | Feira de Tecnologia         | 2026-11-20  | Pátio  | 30    | true               | 19:00:00
-- 2          | Palestra: carreira em dados | 2026-11-25  | [null] | 30    | true               | 19:00:00
-- 3          | Hackathon                   | 2026-12-05  | [null] | 40    | true               | 19:00:00

-- 8. Fim do semestre: apague a tabela inteira. Rode de novo — e depois com IF EXISTS.

DROP TABLE eventos_escola;

-- De novo, sem IF EXISTS (rode só esta linha para ver o erro):
-- DROP TABLE eventos_escola;
-- ERROR: table "eventos_escola" does not exist

DROP TABLE IF EXISTS eventos_escola;

-- NOTICE: table "eventos_escola" does not exist, skipping
-- Com IF EXISTS não há erro, só um aviso: o script segue em frente.

-- PENSE E RESPONDA: No passo 7, quantas vagas tem o Hackathon? E a Feira de Tecnologia?
-- Por que são diferentes?
-- Hackathon: 40. Feira de Tecnologia: 30.
-- O DEFAULT só é usado no momento do INSERT. A Feira entrou quando o padrão era 30;
-- o Hackathon, depois do SET DEFAULT 40. Mudar o DEFAULT não altera as linhas que já existem.
