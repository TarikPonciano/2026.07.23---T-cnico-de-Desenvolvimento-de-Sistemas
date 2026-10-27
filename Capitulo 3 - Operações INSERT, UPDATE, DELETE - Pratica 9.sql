-- CAPÍTULO 3 · GABARITO DA PRÁTICA 9 · Manipulação na biblioteca
-- Banco: biblioteca (montado com o Banco Biblioteca 21-10.sql)
-- Regra da prática: antes de cada UPDATE e DELETE, rode o SELECT com o mesmo WHERE.
-- Se o SELECT mostra as linhas certas, o UPDATE/DELETE vai mexer nelas, e só nelas.


-- 1. Cadastre a editora 4: Editora Nordeste, de Fortaleza.

SELECT * FROM editora;

-- Antes: 3 editoras. O código 4 está livre.

INSERT INTO editora (cod_editora, nome_editora, cidade_editora)
VALUES (4, 'Editora Nordeste', 'Fortaleza');

-- Esperado: INSERT 0 1

-- 2. Cadastre o livro 15: Algoritmos em Python, 2024, ISBN 9786500000106, editora 4.

SELECT * FROM livro;

-- Antes: 5 livros, de 10 a 14.

INSERT INTO livro (cod_livro, titulo_livro, ano_livro, isbn_livro, editora_cod)
VALUES (15, 'Algoritmos em Python', 2024, '9786500000106', 4);

-- Esperado: INSERT 0 1
-- O ISBN vai entre aspas: a coluna é texto, char(13).
-- A editora 4 precisa existir antes: por isso a tarefa 1 vem primeiro.

-- 3. Registre o empréstimo 6: livro 15 para a Júlia (2), informando só o
-- código, o livro e o leitor.

SELECT * FROM emprestimo;

-- Antes: 5 empréstimos, de 1 a 5.

INSERT INTO emprestimo (cod_emprestimo, livro_cod, leitor_cod)
VALUES (6, 15, 2);

-- Esperado: INSERT 0 1
-- Se os testes (g) e (h) da Prática 5 ficaram no banco, os empréstimos 6 e 7 já existem:
-- ERROR: duplicate key value violates unique constraint "emprestimo_pkey"
-- DETAIL: Key (cod_emprestimo)=(6) already exists.
-- Nesse caso, registre como empréstimo 8.

-- 4. A Lia devolveu Dom Casmurro hoje (empréstimo 5): registre a devolução com CURRENT_DATE.

SELECT * FROM emprestimo WHERE cod_emprestimo = 5;

-- Antes: 1 linha, com data_devolucao_emprestimo vazia ([null]).

UPDATE emprestimo
SET data_devolucao_emprestimo = CURRENT_DATE
WHERE cod_emprestimo = 5;

-- Esperado: UPDATE 1
-- CURRENT_DATE = a data do dia em que o comando roda.

-- 5. O Marcos renovou o empréstimo 2: some 1 às renovações.

SELECT * FROM emprestimo WHERE cod_emprestimo = 2;

-- Antes: renovacoes_emprestimo = 1.

UPDATE emprestimo
SET renovacoes_emprestimo = renovacoes_emprestimo + 1
WHERE cod_emprestimo = 2;

-- Esperado: UPDATE 1. Depois: renovacoes_emprestimo = 2.
-- "valor + 1" usa o valor atual da linha: funciona qualquer que seja o número antes.

-- 6. O Rui (4) mudou de turma: agora é ADM-2.

SELECT * FROM leitor WHERE cod_leitor = 4;

-- Antes: 1 linha, Rui Melo, ADM-1.

UPDATE leitor
SET turma_cod = 'ADM-2'
WHERE cod_leitor = 4;

-- Esperado: UPDATE 1
-- Sem o WHERE, TODOS os leitores iriam para a ADM-2.

-- 7. O empréstimo 3 foi lançado por engano: remova.

SELECT * FROM emprestimo WHERE cod_emprestimo = 3;

-- Antes: 1 linha (livro 11, leitora 2).

DELETE FROM emprestimo WHERE cod_emprestimo = 3;

-- Esperado: DELETE 1

-- 8. O Rui Melo (4) saiu da escola. Exclua o leitor — na ordem certa.

SELECT * FROM emprestimo WHERE leitor_cod = 4;

-- Antes: 1 linha (empréstimo 4). O Rui tem um empréstimo registrado.

DELETE FROM emprestimo
WHERE leitor_cod = 4;

-- Esperado: DELETE 1

SELECT * FROM leitor WHERE cod_leitor = 4;

DELETE FROM leitor
WHERE cod_leitor = 4;

-- Esperado: DELETE 1
-- Ordem certa = filhos antes do pai: primeiro os empréstimos do Rui, depois o Rui.
-- Sem FK, o banco aceitaria apagar o leitor primeiro, e o empréstimo 4 ficaria órfão,
-- apontando para um leitor que não existe. No Capítulo 4, a FK passa a cobrar essa ordem.


-- PENSE E RESPONDA: Depois da tarefa 3, consulte o empréstimo 6.
-- De onde vieram a data de retirada e as renovações?

SELECT * FROM emprestimo WHERE cod_emprestimo = 6;

-- Resultado esperado: 1 linha
-- cod_emprestimo | livro_cod | leitor_cod | data_retirada_emprestimo | data_devolucao_emprestimo | renovacoes_emprestimo
-- 6              | 15        | 2          | (data do dia)            | [null]                    | 0
-- Vieram dos DEFAULTs da tabela: data_retirada_emprestimo DEFAULT CURRENT_DATE
-- e renovacoes_emprestimo DEFAULT 0. A devolução não tem DEFAULT: ficou vazia.


-- Conferência final: 4 empréstimos (1, 2, 5 e 6), 3 leitores, 6 livros e 4 editoras.
SELECT * FROM emprestimo ORDER BY cod_emprestimo;
