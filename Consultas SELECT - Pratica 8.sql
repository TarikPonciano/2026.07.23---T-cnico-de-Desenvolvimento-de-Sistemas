-- 1 -  Todos os dados das editoras.
SELECT * FROM editora;

-- 2 - Título e ano de publicação de todos os livros.

SELECT titulo_livro, ano_livro FROM livro;

-- 3 - Os livros publicados antes de 1900.

SELECT * FROM livro WHERE ano_livro < 1900;

-- 4 - As turmas que têm leitores, sem repetir.

SELECT DISTINCT turma_cod FROM leitor;

-- 5 - Os empréstimos que ainda não foram devolvidos.

SELECT * FROM emprestimo WHERE data_devolucao_emprestimo IS NULL;

-- 6 - Os livros cujo título começa com “O”.

SELECT * FROM livro WHERE titulo_livro LIKE 'O%';

-- 7 - Os livros da editora 3, em ordem de título.

SELECT * FROM livro WHERE editora_cod = 3 ORDER BY titulo_livro ASC;

-- 8 - Os 2 livros mais recentes.

SELECT * FROM livro ORDER BY ano_livro DESC LIMIT 2;

-- DESAFIO - Desafio: os empréstimos do leitor 1 que tiveram renovação ou ainda não foram devolvidos. Teste com e
-- sem parênteses.

SELECT * FROM emprestimo WHERE leitor_cod = 1 AND (renovacoes_emprestimo > 0 OR data_devolucao_emprestimo IS NULL);