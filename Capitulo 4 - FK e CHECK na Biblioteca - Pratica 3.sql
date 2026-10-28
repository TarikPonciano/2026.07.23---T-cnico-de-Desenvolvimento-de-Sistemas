-- CAPÍTULO 4 · GABARITO DA PRÁTICA 3 · A biblioteca ganha regras
-- Banco: biblioteca da turma (Banco Biblioteca 21-10.sql, depois das Práticas 8 e 9 do Capítulo 3).
--
-- Nomes: os slides usam os nomes do Capítulo 3 (livros.cod_editora, emprestimos.cod_livro...).
-- Aqui vão os nomes do banco montado em aula:
--   livros.cod_editora        → livro.editora_cod
--   emprestimos.cod_livro     → emprestimo.livro_cod
--   emprestimos.cod_leitor    → emprestimo.leitor_cod
--   renovacoes                → renovacoes_emprestimo
--   data_retirada / devolucao → data_retirada_emprestimo / data_devolucao_emprestimo
--
-- Rode uma vez: criar uma regra que já existe dá "already exists".
-- Para refazer do zero, use os DROP CONSTRAINT do fim do arquivo.
-- Os testes que dão erro de propósito estão comentados, com a mensagem esperada.


-- =====================================================================
-- REGRA 1 · Todo livro é de uma editora cadastrada (FK, pela interface)
-- =====================================================================

-- Na interface: livro → Constraints → botão direito → Create → Foreign Key...
--   General: Name = fk_livro_editora
--   Columns: Local column = editora_cod · References = editora · Referencing = cod_editora → Add
--   Action: deixe NO ACTION (o padrão, que recusa)
-- A aba SQL mostra o comando equivalente:

ALTER TABLE livro
  ADD CONSTRAINT fk_livro_editora
  FOREIGN KEY (editora_cod) REFERENCES editora (cod_editora);

-- Teste (deve ser recusado: a editora 9 não existe).
-- O ISBN vai junto porque, no banco da turma, isbn_livro é NOT NULL:
-- sem ele, o NOT NULL recusaria a linha antes de a FK ser conferida.
-- INSERT INTO livro (cod_livro, titulo_livro, isbn_livro, editora_cod)
-- VALUES (30, 'Memórias Póstumas', '9786500000108', 9);
-- ERROR: insert or update on table "livro" violates foreign key constraint "fk_livro_editora"
-- DETAIL: Key (editora_cod)=(9) is not present in table "editora".


-- =====================================================================
-- REGRA 2 · Todo empréstimo é de um livro cadastrado (FK)
-- =====================================================================

ALTER TABLE emprestimo
  ADD CONSTRAINT fk_emp_livro
  FOREIGN KEY (livro_cod) REFERENCES livro (cod_livro);

-- Teste (deve ser recusado: o livro 99 não existe):
-- INSERT INTO emprestimo (cod_emprestimo, livro_cod, leitor_cod)
-- VALUES (30, 99, 2);
-- ERROR: insert or update on table "emprestimo" violates foreign key constraint "fk_emp_livro"
-- DETAIL: Key (livro_cod)=(99) is not present in table "livro".


-- =====================================================================
-- REGRA 3 · Todo empréstimo é de um leitor cadastrado (FK)
-- =====================================================================

-- A regra 3 não foi criada? Algum empréstimo aponta para um leitor que não existe.
-- O DETAIL do erro diz qual. No caso do teste (g) da Prática 5 do Capítulo 3:
--   ERROR: insert or update on table "emprestimo" violates foreign key constraint "fk_emp_leitor"
--   DETAIL: Key (leitor_cod)=(99) is not present in table "leitor".
-- Confira e apague o órfão, e só depois crie a regra:
-- SELECT * FROM emprestimo WHERE leitor_cod = 99;
-- DELETE FROM emprestimo WHERE leitor_cod = 99;

ALTER TABLE emprestimo
  ADD CONSTRAINT fk_emp_leitor
  FOREIGN KEY (leitor_cod) REFERENCES leitor (cod_leitor);

-- Teste (deve ser recusado: a Lia, leitora 3, ainda tem o empréstimo 5):
-- DELETE FROM leitor WHERE cod_leitor = 3;
-- ERROR: update or delete on table "leitor" violates foreign key constraint "fk_emp_leitor" on table "emprestimo"
-- DETAIL: Key (cod_leitor)=(3) is still referenced from table "emprestimo".


-- =====================================================================
-- REGRA 4 · No máximo 3 renovações, e nunca negativo (CHECK)
-- =====================================================================

-- "De 0 a 3": BETWEEN inclui as duas pontas. Também vale (renovacoes_emprestimo >= 0 AND renovacoes_emprestimo <= 3).
ALTER TABLE emprestimo
  ADD CONSTRAINT ck_renovacoes
  CHECK (renovacoes_emprestimo BETWEEN 0 AND 3);

-- Teste (deve ser recusado: 4 passa do limite):
-- UPDATE emprestimo SET renovacoes_emprestimo = 4
-- WHERE cod_emprestimo = 2;
-- ERROR: new row for relation "emprestimo" violates check constraint "ck_renovacoes"
-- DETAIL: Failing row contains (2, 12, 1, 2026-09-15, null, 4).


-- =====================================================================
-- REGRA 5 · A devolução nunca é antes da retirada (CHECK)
-- =====================================================================

-- A regra compara duas colunas da mesma linha.
-- Empréstimo ainda não devolvido (devolução NULL) passa: NULL não dá falso.
ALTER TABLE emprestimo
  ADD CONSTRAINT ck_devolucao
  CHECK (data_devolucao_emprestimo >= data_retirada_emprestimo);

-- Teste (deve ser recusado: o empréstimo 5 saiu em 2026-10-01):
-- UPDATE emprestimo SET data_devolucao_emprestimo = '2026-09-01'
-- WHERE cod_emprestimo = 5;
-- ERROR: new row for relation "emprestimo" violates check constraint "ck_devolucao"
-- DETAIL: Failing row contains (5, 10, 3, 2026-10-01, 2026-09-01, 0).


-- =====================================================================
-- REGRA 6 · Empréstimo sempre com livro e leitor (NOT NULL, sem nome)
-- =====================================================================

-- No banco da turma, livro_cod e leitor_cod já nasceram NOT NULL.
-- Os comandos rodam sem erro e não mudam nada; num banco sem a regra, eles a criam.
ALTER TABLE emprestimo ALTER COLUMN livro_cod SET NOT NULL;
ALTER TABLE emprestimo ALTER COLUMN leitor_cod SET NOT NULL;

-- Teste (deve ser recusado: falta o leitor):
-- INSERT INTO emprestimo (cod_emprestimo, livro_cod)
-- VALUES (31, 11);
-- ERROR: null value in column "leitor_cod" of relation "emprestimo" violates not-null constraint
-- O NOT NULL não tem nome: a mensagem cita a coluna.


-- =====================================================================
-- CONFERÊNCIA · As regras com nome aparecem em Constraints
-- =====================================================================

-- No pgAdmin: Tables → livro → Constraints e Tables → emprestimo → Constraints.
-- Pelo SQL, a mesma lista:
SELECT conrelid::regclass AS tabela, conname AS regra
FROM pg_constraint
WHERE conname IN ('fk_livro_editora', 'fk_emp_livro', 'fk_emp_leitor', 'ck_renovacoes', 'ck_devolucao')
ORDER BY tabela, regra;

-- Resultado esperado: 5 linhas
-- tabela     | regra
-- livro      | fk_livro_editora
-- emprestimo | ck_devolucao
-- emprestimo | ck_renovacoes
-- emprestimo | fk_emp_leitor
-- emprestimo | fk_emp_livro


-- =====================================================================
-- OS TESTES QUE DEVEM PASSAR
-- =====================================================================

-- Empréstimo 32, com tudo certo: livro 13 e leitora 2 existem, e os DEFAULTs completam a linha.
INSERT INTO emprestimo (cod_emprestimo, livro_cod, leitor_cod)
VALUES (32, 13, 2);

-- Esperado: INSERT 0 1 (retirada = data do dia, renovações = 0)

-- Livro 31, sem editora informada (com ISBN, obrigatório no banco da turma):
INSERT INTO livro (cod_livro, titulo_livro, isbn_livro)
VALUES (31, 'Vidas Secas', '9786500000107');

-- Esperado: INSERT 0 1

SELECT cod_livro, titulo_livro, editora_cod FROM livro WHERE cod_livro = 31;

-- Resultado esperado:
-- cod_livro | titulo_livro | editora_cod
-- 31        | Vidas Secas  | 1


-- PENSE E RESPONDA: O livro 31 passou sem editora, mesmo com a regra 1. Por quê?
-- O que faltaria para recusá-lo?
--
-- Nos nomes dos slides (cod_editora sem NOT NULL): a FK aceita NULL. O livro fica sem
-- editora, e a FK não tem o que conferir. Para recusar: NOT NULL na coluna.
--
-- No banco da turma, o caso é outro: editora_cod é NOT NULL DEFAULT 1. O livro não fica
-- sem editora: recebe a 1, Editora Aurora, sem aviso. A FK aceita, porque a editora 1 existe.
-- Para recusar o livro sem editora, tire o DEFAULT; o NOT NULL passa a barrar:
-- ALTER TABLE livro ALTER COLUMN editora_cod DROP DEFAULT;
-- INSERT INTO livro (cod_livro, titulo_livro, isbn_livro) VALUES (33, 'São Bernardo', '9786500000109');
-- ERROR: null value in column "editora_cod" of relation "livro" violates not-null constraint


-- =====================================================================
-- PARA REFAZER (opcional)
-- =====================================================================

-- Tirar as linhas dos testes que passaram:
-- DELETE FROM emprestimo WHERE cod_emprestimo = 32;
-- DELETE FROM livro WHERE cod_livro = 31;

-- Apagar as regras para criar de novo:
-- ALTER TABLE livro      DROP CONSTRAINT IF EXISTS fk_livro_editora;
-- ALTER TABLE emprestimo DROP CONSTRAINT IF EXISTS fk_emp_livro;
-- ALTER TABLE emprestimo DROP CONSTRAINT IF EXISTS fk_emp_leitor;
-- ALTER TABLE emprestimo DROP CONSTRAINT IF EXISTS ck_renovacoes;
-- ALTER TABLE emprestimo DROP CONSTRAINT IF EXISTS ck_devolucao;
