-- CAPÍTULO 4 · EXEMPLO EM AULA · CREATE TABLE, FK E CHECK · Clínica veterinária
-- Banco: um banco só para o exemplo (ex.: veterinaria).
-- Pode rodar quantas vezes quiser: o script apaga e recria as tabelas.
-- Os comandos que dão erro de propósito estão comentados, com a mensagem esperada:
-- assim o arquivo roda inteiro, de cima a baixo.


-- =====================================================================
-- 1) Apagar: filhos antes dos pais
-- =====================================================================

DROP TABLE IF EXISTS consulta;
DROP TABLE IF EXISTS veterinario;
DROP TABLE IF EXISTS paciente;


-- =====================================================================
-- 2) Criar: pais antes dos filhos
-- =====================================================================

-- paciente: a PK é gerada pelo banco (GENERATED ALWAYS AS IDENTITY).
-- Os CHECKs ficam no fim da tabela, cada um com nome: é o nome que aparece no erro.
CREATE TABLE paciente (
  cod_paciente     integer       GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  nome_paciente    varchar(255)  NOT NULL,
  especie_paciente varchar(255)  NOT NULL DEFAULT 'Silvestre',
  raca_paciente    varchar(255)  DEFAULT 'SRD',
  idade_paciente   integer       DEFAULT 0,
  peso_paciente    numeric(5, 2) DEFAULT 0,
  CONSTRAINT ck_especie_lista CHECK (especie_paciente IN ('Gato', 'Cachorro', 'Silvestre')),
  CONSTRAINT ck_idade_valida  CHECK (idade_paciente >= 0),
  CONSTRAINT ck_peso_valido   CHECK (peso_paciente >= 0)
);

CREATE TABLE veterinario (
  cod_veterinario           integer      GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  nome_veterinario          varchar(255) NOT NULL,
  especialidade_veterinario varchar(255) NOT NULL
);

-- consulta: as duas FKs no fim da tabela, com nome no padrão fk_filha_pai.
-- NOT NULL nas FKs: toda consulta tem paciente e veterinário.
CREATE TABLE consulta (
  cod_consulta    integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  data_consulta   date    NOT NULL DEFAULT CURRENT_DATE,
  paciente_cod    integer NOT NULL,
  veterinario_cod integer NOT NULL,
  CONSTRAINT fk_consulta_paciente    FOREIGN KEY (paciente_cod)    REFERENCES paciente (cod_paciente),
  CONSTRAINT fk_consulta_veterinario FOREIGN KEY (veterinario_cod) REFERENCES veterinario (cod_veterinario)
);

-- Esqueceu uma regra no CREATE TABLE? Com a tabela já criada, ela entra com ALTER TABLE.
-- (Aqui ficam comentados: as regras já existem, e rodar de novo daria "already exists".)
-- ALTER TABLE paciente
--   ADD CONSTRAINT ck_especie_lista CHECK (especie_paciente IN ('Gato', 'Cachorro', 'Silvestre'));
-- ALTER TABLE paciente
--   ADD CONSTRAINT ck_idade_valida CHECK (idade_paciente >= 0);
-- ALTER TABLE paciente
--   ADD CONSTRAINT ck_peso_valido CHECK (peso_paciente >= 0);
-- ALTER TABLE consulta
--   ADD CONSTRAINT fk_consulta_paciente FOREIGN KEY (paciente_cod) REFERENCES paciente (cod_paciente);


-- =====================================================================
-- 3) Dados: pais antes dos filhos
-- =====================================================================

-- Sem informar o código (o banco gera o 1) e sem espécie, raça, idade e peso (vêm os DEFAULTs).
INSERT INTO paciente (nome_paciente)
VALUES ('Toshy');

INSERT INTO veterinario (nome_veterinario, especialidade_veterinario)
VALUES ('Jones Manoel', 'Cachorro');

-- O paciente 1 e o veterinário 1 existem: as duas FKs aceitam. A data vem do DEFAULT.
INSERT INTO consulta (paciente_cod, veterinario_cod)
VALUES (1, 1);

SELECT * FROM paciente;

-- Resultado esperado:
-- cod_paciente | nome_paciente | especie_paciente | raca_paciente | idade_paciente | peso_paciente
-- 1            | Toshy         | Silvestre        | SRD           | 0              | 0.00

SELECT * FROM consulta;

-- Resultado esperado:
-- cod_consulta | data_consulta | paciente_cod | veterinario_cod
-- 1            | (data do dia) | 1            | 1


-- =====================================================================
-- 4) Testes: cada regra recusando um dado errado
-- =====================================================================
-- Rode um teste de cada vez (selecione as linhas e F5) para ver a mensagem.
-- Com GENERATED, todo INSERT recusado gasta um número: os códigos podem pular.

-- Peso negativo, o teste feito em aula:
-- INSERT INTO paciente (nome_paciente, especie_paciente, peso_paciente, idade_paciente)
-- VALUES ('Leo', 'Silvestre', -120, 3);
-- ERROR: new row for relation "paciente" violates check constraint "ck_peso_valido"
-- DETAIL: Failing row contains (2, Leo, Silvestre, SRD, 3, -120.00).

-- Espécie fora da lista:
-- INSERT INTO paciente (nome_paciente, especie_paciente)
-- VALUES ('Nemo', 'Peixe');
-- ERROR: new row for relation "paciente" violates check constraint "ck_especie_lista"

-- Idade negativa:
-- INSERT INTO paciente (nome_paciente, idade_paciente)
-- VALUES ('Bidu', -1);
-- ERROR: new row for relation "paciente" violates check constraint "ck_idade_valida"

-- Consulta de um paciente que não existe:
-- INSERT INTO consulta (paciente_cod, veterinario_cod)
-- VALUES (99, 1);
-- ERROR: insert or update on table "consulta" violates foreign key constraint "fk_consulta_paciente"
-- DETAIL: Key (paciente_cod)=(99) is not present in table "paciente".

-- Excluir o paciente que tem consulta (filhos antes do pai):
-- DELETE FROM paciente WHERE cod_paciente = 1;
-- ERROR: update or delete on table "paciente" violates foreign key constraint "fk_consulta_paciente" on table "consulta"
-- DETAIL: Key (cod_paciente)=(1) is still referenced from table "consulta".

-- Informar o código à mão, com GENERATED ALWAYS:
-- INSERT INTO paciente (cod_paciente, nome_paciente)
-- VALUES (10, 'Rex');
-- ERROR: cannot insert a non-DEFAULT value into column "cod_paciente"
-- DETAIL: Column "cod_paciente" is an identity column defined as GENERATED ALWAYS.
