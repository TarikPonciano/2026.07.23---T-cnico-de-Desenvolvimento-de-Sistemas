# Capítulo 5 · Gabarito das Práticas 2 e 4 (banco cinema)

As mensagens abaixo foram conferidas com psycopg 3.3 e PostgreSQL 15, no banco montado pelo `setup_cinema.py`.

Nos trechos que passam pela classe `Banco`, o `except` genérico dela imprime antes a linha
`Erro no banco: ...`, com a mesma mensagem, e repassa o erro com `raise`.

## Prática 2 · Encontre o erro

| Trecho | O que acontece | Correção |
|---|---|---|
| **a** `(cod)` | Erro. Sem a vírgula, `(cod)` é só o número 2 entre parênteses, não uma tupla: `TypeError: object of type 'int' has no len()` | `(cod,)` |
| **b** `'%s'` | Erro. Com aspas, o `%s` fica dentro de um texto e o banco não sabe o tipo do valor: `psycopg.errors.IndeterminateDatatype: could not determine data type of parameter $1` | `WHERE classificacao_filme = %s`, sem aspas |
| **c** `%d` | Erro. O psycopg só aceita `%s`: `psycopg.ProgrammingError: only '%s', '%b', '%t' are allowed as placeholders, got '%d'` | `%s` |
| **d** `(5,)` | Erro. Dois `%s` e um valor só: `psycopg.ProgrammingError: the query has 2 placeholders but 1 parameters were passed` | `(5, cod_sessao)` |
| **e** f-string | Erro. O título entra no SQL sem aspas: `syntax error at or near "sem"`. Com aspas, funcionaria, mas aceitaria SQL injection. | `WHERE titulo_filme = %s` e `(titulo,)` |
| **f** ILIKE sem `%` | Resultado errado, sem erro: `[]`. `ILIKE 'farol'` só acha o título que é exatamente "farol". | `("%" + termo + "%",)` → `[('O Último Farol',)]` |
| **g** sem commit | Resultado errado, sem erro: imprime "Sessão excluída!", mas a sessão 6 continua no banco. O `close()` sem `commit()` desfaz o DELETE. | `conexao.commit()` antes do `close()`, ou `banco.executar(...)` |
| **h** `[cod]` | **Certo.** Uma lista também serve para os parâmetros: `[('Corrida nas Dunas',)]` | — |

## Prática 4 · Qual mensagem aparece?

Programa: `cadastrar_filme.py`. Cada chamada termina com `---`, impresso pelo `finally`.
Nas chamadas recusadas, a classe imprime antes a linha `Erro no banco: ...` (com o DETAIL).

| Chamada | O que a classe imprime | Mensagem do programa | Por quê |
|---|---|---|---|
| **a** `("Maré Alta", 101, "12")` | — | `Filme cadastrado: Maré Alta` | Tudo dentro das regras. |
| **b** `("Maré Alta", 0, "12")` | `Erro no banco: new row for relation "filmes" violates check constraint "ck_duracao"` | `Duração inválida.` | `CheckViolation` em `ck_duracao` (duração maior que zero). |
| **c** `("Maré Alta", 101, "13")` | `Erro no banco: new row for relation "filmes" violates check constraint "ck_classificacao"` | `Classificação inválida.` | `CheckViolation` em `ck_classificacao` (13 não está na lista). |
| **d** `(None, 101, "L")` | `Erro no banco: null value in column "titulo_filme" of relation "filmes" violates not-null constraint` | `Faltou um dado obrigatório.` | `None` vira `NULL`, e o `NOT NULL` do título recusa: `NotNullViolation`. |
| **e** `("Maré Alta", 101, "Livre")` | `Erro no banco: value too long for type character varying(2)` | `Não foi possível cadastrar.` | `"Livre"` não cabe em `varchar(2)`. É um `DataError` (`StringDataRightTruncation`), que nenhum `except` específico pega; o `psycopg.Error` pega. |
| **f** `("Maré Alta", 101, "12")` | — | `Filme cadastrado: Maré Alta` | Nenhuma regra impede o título repetido. |

**Pense e responda:** faltou um `UNIQUE` no título:
`CONSTRAINT uq_titulo_filme UNIQUE (titulo_filme)`. Com ele, a chamada **f** daria `UniqueViolation`,
e caberia um `except psycopg.errors.UniqueViolation:` com a mensagem "Filme já cadastrado."
