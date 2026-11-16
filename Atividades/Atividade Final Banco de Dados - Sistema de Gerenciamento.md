# Atividade de Conclusão da Unidade — Sistema de Gerenciamento com Banco de Dados

## Modalidade

**Individual**

## Objetivo

Reunir tudo o que foi construído na unidade num sistema próprio: da ideia do negócio ao programa em Python conectado ao PostgreSQL. Você vai **idealizar um cenário**, **modelar** o banco, **implementar** o banco com um script e construir um **sistema de gerenciamento** com CRUD, consultas com JOIN e uma regra de negócio.

---

## O que você já sabe fazer

Cada etapa da atividade usa o que foi visto nos capítulos:

| Etapa da atividade | Onde foi visto |
|--------------------|----------------|
| Descrever o cenário, identificar entidades, relacionamentos e cardinalidade | Capítulos 1 e 2 |
| DER em notação de Chen, MER e formas normais | Capítulo 2 |
| Banco na Aiven, pgAdmin, `SELECT`, `INSERT`, `UPDATE` e `DELETE` | Capítulo 3 |
| `CREATE TABLE`, `GENERATED ALWAYS AS IDENTITY`, `FOREIGN KEY`, `CHECK`, `UNIQUE` e `JOIN` | Capítulo 4 |
| `.env`, psycopg, script de setup, `classBanco.py`, CRUD com menu, `RETURNING` e transação | Capítulo 5 |

---

## Etapa 1 · O cenário

Idealize um negócio ou uma organização que precisa de um sistema para gerenciar seus dados. Escreva um **briefing** de um ou dois parágrafos, no mesmo estilo dos cenários trabalhados em aula, respondendo:

- Que negócio é esse e quem vai usar o sistema?
- O que precisa ser guardado? (Ex.: os produtos, os clientes, as vendas.)
- Como essas informações se relacionam? (Ex.: cada venda é de um cliente e tem vários produtos.)
- Que **regras** o negócio tem? (Ex.: o estoque nunca fica negativo; um cliente não pode ter mais de 3 locações abertas.)

Algumas ideias para inspirar: pizzaria, farmácia, pousada, pet shop, salão de beleza, cantina escolar, sebo, restaurante com comandas, locadora de carros, floricultura, lava-jato, agência de viagens, doceria, distribuidora de água e gás, brechó, ótica, locadora de jogos, hortifruti.

**Entregável:** o briefing no `README.md` do projeto.

---

## Etapa 2 · DER e MER

A partir do briefing:

1. Liste as **entidades**, os **relacionamentos** (com o verbo) e a **cardinalidade** de cada um.
2. Desenhe o **DER** em notação de Chen, no draw.io: entidades, losangos com o verbo e 1/N.
3. Monte o **MER**: todas as tabelas, com colunas, tipos, PK e FK, ligadas com 1 e N.
4. Relacionamento N:N vira uma **tabela de ligação**, com as duas FKs.
5. Confira as formas normais: nenhuma coluna com lista de valores, nenhum dado repetido que deveria estar em outra tabela.

**Entregável:** as imagens do DER e do MER (PNG ou SVG) e o arquivo `.drawio`.

---

## Etapa 3 · O banco: `setup.py`

O banco planejado deve ter **pelo menos 3 tabelas distintas**, ligadas por chaves estrangeiras.

### Regras do banco

- Toda tabela com **PK própria**, gerada pelo banco: `GENERATED ALWAYS AS IDENTITY`.
- As tabelas ligadas por **FKs com nome** (`CONSTRAINT fk_...`): no mínimo 2.
- Pelo menos um **`CHECK`** e um **`UNIQUE`** com nome, vindos das regras do briefing.
- `NOT NULL` em toda coluna obrigatória.

### O script

Crie o `setup.py` no molde do `setup_rh.py`:

- Os dados da conexão vêm do `.env` (`DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_SSL`).
- Tudo dentro de `try/except/finally`: `rollback()` no `except`, e o cursor e a conexão fechados no `finally`.
- `DROP TABLE IF EXISTS` com os **filhos antes dos pais**; `CREATE TABLE` com os **pais antes dos filhos**.
- **As chaves estrangeiras e os `CHECK` implementados no `CREATE TABLE`**, cada um com `CONSTRAINT` e nome, como no `setup_rh.py`:

  ```sql
  CONSTRAINT ck_preco_positivo CHECK (preco > 0),
  CONSTRAINT fk_produto_categoria FOREIGN KEY (cod_categoria) REFERENCES categorias (cod_categoria)
  ```

- `INSERT` com os **dados iniciais**: pelo menos **5 registros em cada tabela**, pensados para testar o JOIN e a regra de negócio. Os dados iniciais precisam respeitar as FKs e os `CHECK`: se algum for recusado, o `rollback()` desfaz o script inteiro.
- `commit()` no fim.

O script deve rodar **duas vezes seguidas sem erro**: o banco sempre começa do zero.

**Teste as regras no pgAdmin**, depois de rodar o `setup.py`. Cada uma deve recusar um dado errado:

- um `INSERT` com uma FK que não existe (ex.: `cod_categoria` 99) é recusado pela chave estrangeira;
- um `INSERT` que fere o `CHECK` (ex.: preço negativo) é recusado pelo `CHECK`;
- um `DELETE` de um registro que tem filhos ligados a ele é recusado pela chave estrangeira.

---

## Etapa 4 · O sistema: `classBanco.py` e `main.py`

### `classBanco.py`

Use a classe `Banco` do Capítulo 5, com os métodos `consultar` (SELECT) e `manipular` (INSERT, UPDATE e DELETE). Você pode acrescentar métodos novos, como o `registrarVenda` da Loja Conecta.

### `main.py`

Um menu no terminal, com `while True`, que interage com o banco por meio da classe.

**CRUD simples de todas as tabelas.** Para cada tabela, implemente:

| Operação | O que faz |
|----------|-----------|
| **Ver** | Lista todos os registros |
| **Cadastrar** | Pede os dados e faz o `INSERT` |
| **Alterar** | Escolhe um registro pelo código e faz o `UPDATE` (deixe vazio para manter o valor atual) |
| **Remover** | Escolhe um registro pelo código, pede confirmação e faz o `DELETE` |

A função de escolher um registro (como o `escolherFuncionario`) mostra a ficha dele e serve ao alterar e ao remover.

**Regras do código:**

- Todo valor digitado entra no SQL por **`%s`**, nunca colado com f-string.
- Toda operação que grava no banco fica dentro de `try/except`, com uma mensagem que o usuário entende. Exemplo: remover um registro que tem filhos ligados a ele é recusado pela FK, e o sistema avisa.
- **Nenhuma opção do menu pode terminar em Traceback.**

---

## Etapa 5 · Pelo menos uma operação com JOIN

O sistema deve ter **pelo menos uma** opção que junta tabelas com `JOIN`. Exemplos:

- Uma listagem que mostra o **nome** no lugar do código (ex.: os produtos com o nome da categoria).
- Um relatório com dados de duas ou mais tabelas (ex.: as vendas de um cliente, com os produtos de cada uma).
- “Quem não tem”: `LEFT JOIN` com `IS NULL` (ex.: os clientes que nunca compraram).

---

## Etapa 6 · Pelo menos uma operação de regra de negócio

Além do CRUD, o sistema deve ter **pelo menos uma** operação inspirada numa regra do seu negócio: o sistema **decide**, **calcula** ou **impede** alguma coisa. Explique no `README.md` qual é a regra, por que ela existe e como testar.

### Sugestões

| Regra | Exemplo | O que você vai usar |
|-------|---------|---------------------|
| **Controle de estoque** | Ao registrar uma venda, baixar o estoque. Venda maior que o estoque é recusada. | `UPDATE ... SET estoque = estoque - %s`, `CHECK (estoque >= 0)`, transação |
| **Movimento com itens** | Registrar um pedido, uma reserva ou um atendimento junto com os seus itens: tudo ou nada. | `INSERT ... RETURNING`, um método novo na classe (como o `registrarVenda`), `rollback()` |
| **Limite por cliente** | Um cliente não pode ter mais de 3 locações (ou empréstimos) em aberto. | `SELECT` antes do `INSERT`, `len()` da lista no Python |
| **Disponibilidade** | Não permitir duas reservas do mesmo quarto (ou horário, ou mesa) na mesma data. | `SELECT` antes do `INSERT`, ou `UNIQUE` em duas colunas |
| **Fluxo de status** | Um pedido vai de “aberto” para “enviado” e depois “entregue”; o que já foi entregue não pode ser cancelado. | `CHECK (status IN (...))`, consultar o status atual antes do `UPDATE` |
| **Total com desconto** | Calcular o total de um pedido (ou comanda); acima de R$ 200, desconto de 10%. | `SELECT` dos itens com JOIN, soma no `for`, a regra no Python |
| **Multa por atraso** | A devolução depois da data prevista paga uma multa por dia de atraso. | Datas do banco como `date`, a diferença em dias no Python |
| **Reajuste em lote** | Reajustar em X% os preços de uma categoria (ou os salários de um setor). | `UPDATE ... WHERE cod_categoria = %s` com dois parâmetros, `rowcount` |
| **Alertas** | Listar os produtos com estoque abaixo do mínimo, ou os clientes sem nenhuma compra. | `WHERE` com comparação, `LEFT JOIN` com `IS NULL` |
| **Pontos de fidelidade** | Cada compra soma pontos ao cliente; ao chegar a 100 pontos, a próxima compra tem desconto. | Uma coluna de pontos, `UPDATE` depois da compra, a regra no Python |

> Para somar ou contar, percorra as linhas no Python, como no `verVenda` da Loja Conecta: `total = total + subtotal`.

---

## Estrutura Sugerida

```
meu-sistema/
├── README.md          o briefing, a regra de negócio e como rodar
├── .gitignore         com a linha .env
├── .env.exemplo       o modelo do .env, sem a senha
├── modelagem/
│   ├── der.png
│   ├── mer.png
│   └── modelagem.drawio
├── setup.py           apaga, cria e preenche o banco
├── classBanco.py      a classe Banco
└── main.py            o sistema
```

```python
from classBanco import Banco

banco = Banco()

# ---- Tabela 1 ----
def verClientes(): ...
def escolherCliente(): ...
def cadastrarCliente(): ...
def alterarCliente(): ...
def removerCliente(): ...

# ---- Tabela 2 ----
# ... as mesmas operações

# ---- Tabela 3 ----
# ... as mesmas operações

# ---- JOIN e regra de negócio ----
def relatorioVendas(): ...     # a operação com JOIN
def registrarVenda(): ...      # a regra de negócio

# ---- Menu principal ----
while (True):
    # 1 a 5: tabela 1 · 11 a 15: tabela 2 · 21 a 25: tabela 3
    # 31 em diante: relatórios e regras de negócio · 0: sair
    ...
```

---

## Entrega

O link de um **repositório no GitHub** com tudo o que está na estrutura sugerida.

O **`.env` não vai para o GitHub**: ele tem a sua senha. Confira no `git status` antes de cada commit; o `.env` não pode aparecer na lista.

---

## Checklist de Requisitos

Antes de entregar, confira se o trabalho atende a todos os pontos:

- [ ] O cenário está descrito no `README.md`
- [ ] O DER (notação de Chen) e o MER estão no repositório
- [ ] O banco tem **pelo menos 3 tabelas**, ligadas por FKs
- [ ] Toda PK usa `GENERATED ALWAYS AS IDENTITY`
- [ ] As **chaves estrangeiras** e os **`CHECK`** estão implementados no `setup.py`, com nome
- [ ] O `UNIQUE` está implementado, com nome
- [ ] Testei no pgAdmin: cada FK e cada `CHECK` recusa um dado errado
- [ ] Cada tabela tem pelo menos 5 registros iniciais
- [ ] O `setup.py` roda duas vezes seguidas sem erro
- [ ] O `.env` está fora do GitHub, e o `.env.exemplo` está no repositório
- [ ] O `classBanco.py` tem `consultar` e `manipular`
- [ ] Todas as tabelas têm CRUD: ver, cadastrar, alterar e remover
- [ ] Há pelo menos uma operação com **JOIN**
- [ ] Há pelo menos uma operação de **regra de negócio**, explicada no `README.md`
- [ ] Todo valor digitado entra no SQL por `%s`
- [ ] Nenhuma opção do menu termina em Traceback

---

## Dicas

1. **Comece pequeno:** 3 tabelas bem feitas valem mais que 8 pela metade. Dá para crescer depois.
2. **Mostre o MER ao professor antes do `setup.py`:** um MER certo poupa horas de `ALTER TABLE`.
3. **Teste o SQL no pgAdmin primeiro:** funcionou lá? Cole no Python.
4. **Faça o CRUD de uma tabela inteira e teste:** depois repita o molde nas outras, com atenção à ordem dos `%s`.
5. **Pense nos dados iniciais junto com a regra de negócio:** deixe casos em que a regra aceita e casos em que ela recusa.
6. **Faça commits com frequência**, sempre conferindo o `git status`.
