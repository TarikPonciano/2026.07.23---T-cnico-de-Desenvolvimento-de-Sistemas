-- CAPÍTULO 3 · GABARITO DA PRÁTICA 8 · Consultas na biblioteca
-- Banco: biblioteca (montado com o Banco Biblioteca 21-10.sql)
-- Os resultados esperados valem para os dados da Prática 4, antes da Prática 9.
-- Se testes da Prática 5 ficaram no banco, algumas consultas trazem linhas a mais.


-- 1. Todos os dados das editoras.

SELECT * FROM editora;

-- Resultado esperado: 3 linhas
-- cod_editora | nome_editora      | cidade_editora
-- 1           | Editora Aurora    | Recife
-- 2           | Editora Horizonte | São Paulo
-- 3           | Editora Código    | Recife

-- 2. Título e ano de publicação de todos os livros.

SELECT titulo_livro, ano_livro FROM livro;

-- Resultado esperado: 5 linhas, só as duas colunas pedidas
-- titulo_livro             | ano_livro
-- Dom Casmurro             | 1899
-- O Cortiço                | 1890
-- Iracema                  | 1865
-- Lógica de Programação    | 2019
-- Banco de Dados Essencial | 2021

-- 3. Os livros publicados antes de 1900.

SELECT * FROM livro WHERE ano_livro < 1900;

-- Resultado esperado: 3 linhas (Dom Casmurro, O Cortiço e Iracema)
-- "Antes de 1900" não inclui 1900: por isso < e não <=.

-- 4. As turmas que têm leitores, sem repetir.

SELECT DISTINCT turma_cod FROM leitor;

-- Resultado esperado: 3 linhas (TDS-1, TDS-2 e ADM-1)
-- O Marcos e a Lia são da TDS-1: sem DISTINCT, ela apareceria duas vezes.
-- Sem ORDER BY, a ordem das linhas pode variar.

-- 5. Os empréstimos que ainda não foram devolvidos.

SELECT * FROM emprestimo WHERE data_devolucao_emprestimo IS NULL;

-- Resultado esperado: 3 linhas (empréstimos 2, 3 e 5)
-- Para NULL, use IS NULL. Com "= NULL" a consulta não dá erro, mas volta vazia.

-- 6. Os livros cujo título começa com "O".

SELECT * FROM livro WHERE titulo_livro LIKE 'O%';

-- Resultado esperado: 1 linha (O Cortiço)
-- % = qualquer texto depois do "O". O LIKE diferencia maiúsculas:
-- com 'o%' a consulta volta vazia. Para ignorar maiúsculas, use ILIKE.

-- 7. Os livros da editora 3, em ordem de título.

SELECT * FROM livro WHERE editora_cod = 3 ORDER BY titulo_livro ASC;

-- Resultado esperado: 2 linhas
-- cod_livro | titulo_livro             | isbn_livro    | ano_livro | editora_cod
-- 14        | Banco de Dados Essencial | 9786500000105 | 2021      | 3
-- 13        | Lógica de Programação    | 9786500000104 | 2019      | 3
-- ASC é o padrão do ORDER BY: pode ser omitido.

-- 8. Os 2 livros mais recentes.

SELECT * FROM livro ORDER BY ano_livro DESC LIMIT 2;

-- Resultado esperado: 2 linhas (Banco de Dados Essencial, 2021, e Lógica de Programação, 2019)
-- Primeiro ordena do mais novo para o mais antigo (DESC), depois corta em 2 (LIMIT).
-- Sem o ORDER BY, o LIMIT 2 traria duas linhas quaisquer.


-- DESAFIO: os empréstimos do leitor 1 que tiveram renovação ou ainda não foram devolvidos.
-- Teste com e sem parênteses.

-- Com parênteses (o certo):
SELECT * FROM emprestimo WHERE leitor_cod = 1 AND (renovacoes_emprestimo > 0 OR data_devolucao_emprestimo IS NULL);

-- Resultado esperado: 1 linha (empréstimo 2: do leitor 1, com 1 renovação e sem devolução)

-- Sem parênteses:
SELECT * FROM emprestimo WHERE leitor_cod = 1 AND renovacoes_emprestimo > 0 OR data_devolucao_emprestimo IS NULL;

-- Resultado esperado: 3 linhas (empréstimos 2, 3 e 5)
-- O AND é resolvido antes do OR. Sem parênteses, o banco lê:
--   (leitor 1 E com renovação) OU (sem devolução, de qualquer leitor)
-- e traz também os empréstimos 3 e 5, que não são do leitor 1.
