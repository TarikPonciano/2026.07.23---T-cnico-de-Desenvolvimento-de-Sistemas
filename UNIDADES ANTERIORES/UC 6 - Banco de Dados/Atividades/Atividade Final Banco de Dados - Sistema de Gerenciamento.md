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

### O exemplo deste documento

Cada etapa traz um **exemplo** com o mesmo cenário: a **Locadora de Jogos Joystick**. Ele mostra o formato esperado de cada entrega. O seu sistema é do **seu** cenário: use o exemplo como modelo, não como resposta.

---

## Etapa 1 · O cenário

Idealize um negócio ou uma organização que precisa de um sistema para gerenciar seus dados. Escreva um **briefing** de um ou dois parágrafos, no mesmo estilo dos cenários trabalhados em aula, respondendo:

- Que negócio é esse e quem vai usar o sistema?
- O que precisa ser guardado? (Ex.: os produtos, os clientes, as vendas.)
- Como essas informações se relacionam? (Ex.: cada venda é de um cliente e tem vários produtos.)
- Que **regras** o negócio tem? (Ex.: o estoque nunca fica negativo; um cliente não pode ter mais de 3 locações abertas.)

Algumas ideias para inspirar: pizzaria, farmácia, pousada, pet shop, salão de beleza, cantina escolar, sebo, restaurante com comandas, locadora de carros, floricultura, lava-jato, agência de viagens, doceria, distribuidora de água e gás, brechó, ótica, locadora de jogos, hortifruti.

**Entregável:** o briefing no `README.md` do projeto.

### Exemplo · Locadora de Jogos Joystick

> A Locadora Joystick aluga jogos de PS5, Xbox, Switch e PC. Cadastramos os **clientes** (nome, e-mail e telefone) e os **jogos** (título, plataforma e preço da diária). Cada **aluguel** é de um cliente e de um jogo, com a data de retirada, a data prevista para a devolução e a data em que o jogo voltou. Um cliente aluga vários jogos, e o mesmo jogo é alugado por vários clientes ao longo do tempo.

**Regras do negócio:**

- O e-mail do cliente não se repete.
- A plataforma é PS5, Xbox, Switch ou PC, e a diária é maior que zero.
- A data prevista para a devolução nunca é antes da retirada.
- Um cliente pode ter, no máximo, **3 aluguéis em aberto** (sem devolução).

---

## Etapa 2 · DER e MER

A partir do briefing:

1. Liste as **entidades**, os **relacionamentos** (com o verbo) e a **cardinalidade** de cada um.
2. Desenhe o **DER** em notação de Chen, no draw.io: entidades, losangos com o verbo e 1/N.
3. Monte o **MER**: todas as tabelas, com colunas, tipos, PK e FK, ligadas com 1 e N.
4. Relacionamento N:N vira uma **tabela de ligação**, com as duas FKs.
5. Confira as formas normais: nenhuma coluna com lista de valores, nenhum dado repetido que deveria estar em outra tabela.

**Entregável:** as imagens do DER e do MER (PNG ou SVG) e o arquivo `.drawio`.

### Exemplo · Entidades e relacionamentos

| Relacionamento | Verbo | Cardinalidade |
|----------------|-------|---------------|
| CLIENTE e JOGO | aluga | **N:N**: um cliente aluga vários jogos; um jogo é alugado por vários clientes |

### Exemplo · DER (notação de Chen)

```
[ CLIENTE ] ──── N ──── < aluga > ──── N ──── [ JOGO ]
```

No draw.io: CLIENTE e JOGO em retângulos, **aluga** num losango, e N nos dois lados da ligação.

### Exemplo · MER

O N:N **aluga** vira a tabela `alugueis`, com uma FK para cada lado:

```
clientes  1 ──── N  alugueis  N ──── 1  jogos
```

**clientes**

| Coluna | Tipo | Regra |
|--------|------|-------|
| `cod_cliente` | INTEGER | PK, gerada pelo banco |
| `nome_cliente` | VARCHAR(100) | obrigatório |
| `email_cliente` | VARCHAR(100) | obrigatório · `UNIQUE` |
| `telefone_cliente` | CHAR(11) | obrigatório |

**jogos**

| Coluna | Tipo | Regra |
|--------|------|-------|
| `cod_jogo` | INTEGER | PK, gerada pelo banco |
| `titulo_jogo` | VARCHAR(100) | obrigatório |
| `plataforma_jogo` | VARCHAR(10) | obrigatório · `CHECK`: PS5, Xbox, Switch ou PC |
| `preco_diaria` | NUMERIC(6,2) | obrigatório · `CHECK`: maior que zero |

**alugueis**

| Coluna | Tipo | Regra |
|--------|------|-------|
| `cod_aluguel` | INTEGER | PK, gerada pelo banco |
| `cod_cliente` | INTEGER | obrigatório · **FK** para `clientes` |
| `cod_jogo` | INTEGER | obrigatório · **FK** para `jogos` |
| `data_retirada` | DATE | obrigatório · padrão: a data do dia |
| `data_prevista` | DATE | obrigatório · `CHECK`: não pode ser antes da retirada |
| `data_devolucao` | DATE | opcional: vazia enquanto o jogo não volta |

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
- **As chaves estrangeiras e os `CHECK` implementados no `CREATE TABLE`**, cada um com `CONSTRAINT` e nome, como no `setup_rh.py`.
- `INSERT` com os **dados iniciais**: pelo menos **5 registros em cada tabela**, pensados para testar o JOIN e a regra de negócio. Os dados iniciais precisam respeitar as FKs e os `CHECK`: se algum for recusado, o `rollback()` desfaz o script inteiro.
- `commit()` no fim.

O script deve rodar **duas vezes seguidas sem erro**: o banco sempre começa do zero.

**Teste as regras no pgAdmin**, depois de rodar o `setup.py`. Cada uma deve recusar um dado errado:

- um `INSERT` com uma FK que não existe é recusado pela chave estrangeira;
- um `INSERT` que fere o `CHECK` é recusado pelo `CHECK`;
- um `DELETE` de um registro que tem filhos ligados a ele é recusado pela chave estrangeira.

### Exemplo · Trechos do `setup.py` da Locadora Joystick

A ordem: `alugueis` depende de `clientes` e de `jogos`, então ela sai primeiro e é criada por último.

```python
    # Apagar: filhos antes dos pais
    cursor.execute("DROP TABLE IF EXISTS alugueis;")
    cursor.execute("DROP TABLE IF EXISTS jogos;")
    cursor.execute("DROP TABLE IF EXISTS clientes;")
    print("REMOÇÃO DE TABELAS ANTIGAS CONCLUÍDA")

    # Criar: pais antes dos filhos (clientes e jogos antes de alugueis)
    cursor.execute('''
        CREATE TABLE clientes(
            cod_cliente INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            nome_cliente VARCHAR(100) NOT NULL,
            email_cliente VARCHAR(100) NOT NULL,
            telefone_cliente CHAR(11) NOT NULL,
            CONSTRAINT uq_cliente_email UNIQUE (email_cliente)
        );
    ''')
    cursor.execute('''
        CREATE TABLE jogos(
            cod_jogo INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            titulo_jogo VARCHAR(100) NOT NULL,
            plataforma_jogo VARCHAR(10) NOT NULL,
            preco_diaria NUMERIC(6,2) NOT NULL,
            CONSTRAINT ck_jogo_plataforma CHECK (plataforma_jogo IN ('PS5', 'Xbox', 'Switch', 'PC')),
            CONSTRAINT ck_jogo_preco CHECK (preco_diaria > 0)
        );
    ''')
    cursor.execute('''
        CREATE TABLE alugueis(
            cod_aluguel INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            cod_cliente INTEGER NOT NULL,
            cod_jogo INTEGER NOT NULL,
            data_retirada DATE NOT NULL DEFAULT CURRENT_DATE,
            data_prevista DATE NOT NULL,
            data_devolucao DATE,
            CONSTRAINT ck_aluguel_datas CHECK (data_prevista >= data_retirada),
            CONSTRAINT fk_aluguel_cliente FOREIGN KEY (cod_cliente) REFERENCES clientes (cod_cliente),
            CONSTRAINT fk_aluguel_jogo FOREIGN KEY (cod_jogo) REFERENCES jogos (cod_jogo)
        );
    ''')
    print("TABELAS CRIADAS COM SUCESSO!")
```

Os dados iniciais foram pensados para os testes: a Ana (cliente 1) já tem 3 aluguéis em aberto, para testar a regra de negócio, e o Diego, a Eva e o jogo Galáxia Zero não têm nenhum aluguel.

```python
    cursor.execute('''
        INSERT INTO alugueis (cod_cliente, cod_jogo, data_retirada, data_prevista, data_devolucao)
        VALUES (1, 1, '2026-11-02', '2026-11-05', '2026-11-05'),
               (1, 2, '2026-11-10', '2026-11-13', NULL),
               (1, 3, '2026-11-12', '2026-11-15', NULL),
               (1, 4, '2026-11-14', '2026-11-17', NULL),
               (2, 1, '2026-11-11', '2026-11-14', '2026-11-16'),
               (3, 2, '2026-11-15', '2026-11-18', NULL);
    ''')
```

O resultado, rodando duas vezes:

```
> python setup.py
REMOÇÃO DE TABELAS ANTIGAS CONCLUÍDA
TABELAS CRIADAS COM SUCESSO!
DADOS INSERIDOS.
```

### Exemplo · Testes das regras no pgAdmin

| Teste | O que o banco responde |
|-------|------------------------|
| `INSERT INTO alugueis (cod_cliente, cod_jogo, data_prevista) VALUES (99, 1, '2026-11-20');` | `violates foreign key constraint "fk_aluguel_cliente"`: o cliente 99 não existe |
| `INSERT INTO jogos (titulo_jogo, plataforma_jogo, preco_diaria) VALUES ('Teste', 'Atari', 5);` | `violates check constraint "ck_jogo_plataforma"`: Atari não está na lista |
| `DELETE FROM clientes WHERE cod_cliente = 1;` | `violates foreign key constraint "fk_aluguel_cliente" on table "alugueis"`: a Ana tem aluguéis |

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

### Exemplo · O menu da Locadora Joystick

```
    LOCADORA JOYSTICK

    1. Ver Clientes          11. Ver Jogos            21. Ver Aluguéis
    2. Escolher Cliente      12. Escolher Jogo        22. Escolher Aluguel
    3. Cadastrar Cliente     13. Cadastrar Jogo       23. Cadastrar Aluguel
    4. Alterar Cliente       14. Alterar Jogo         24. Alterar Aluguel
    5. Remover Cliente       15. Remover Jogo         25. Remover Aluguel

    0. Sair
```

### Exemplo · Ver e cadastrar jogos

```python
from classBanco import Banco

banco = Banco()


def verJogos():
    print("LISTA DE JOGOS")

    jogos = banco.consultar('''
        SELECT cod_jogo, titulo_jogo, plataforma_jogo, preco_diaria
        FROM jogos
        ORDER BY cod_jogo;
    ''')

    if (len(jogos) == 0):
        print("NÃO HÁ JOGOS CADASTRADOS")
        return

    print("Código | Título | Plataforma | Diária")
    for cod, titulo, plataforma, preco in jogos:
        print(f"{cod} | {titulo} | {plataforma} | R$ {preco:,.2f}")


def cadastrarJogo():
    print("CADASTRO DE NOVO JOGO")

    titulo = input("Digite o título do jogo: ")
    plataforma = input("Digite a plataforma (PS5, Xbox, Switch ou PC): ")
    preco = float(input("Digite o preço da diária: "))

    try:
        banco.manipular('''
            INSERT INTO jogos
            VALUES (default, %s, %s, %s);
        ''', (titulo, plataforma, preco))
        print("JOGO CADASTRADO COM SUCESSO!")
    except Exception as error:
        print("ERRO AO CADASTRAR JOGO")
```

Com uma plataforma fora da lista, o `CHECK` recusa, a classe mostra a mensagem do banco e o programa avisa o usuário:

```
CADASTRO DE NOVO JOGO
Digite o título do jogo: Mundo Aberto
Digite a plataforma (PS5, Xbox, Switch ou PC): Atari
Digite o preço da diária: 10
ERRO DE MANIPULAÇÃO: new row for relation "jogos" violates check constraint "ck_jogo_plataforma"
DETAIL:  Failing row contains (8, Mundo Aberto, Atari, 10.00).
ERRO AO CADASTRAR JOGO
```

As outras operações (escolher, alterar e remover) seguem o molde do CRUD do Sistema RH.

---

## Etapa 5 · Pelo menos uma operação com JOIN

O sistema deve ter **pelo menos uma** opção que junta tabelas com `JOIN`. Exemplos:

- Uma listagem que mostra o **nome** no lugar do código (ex.: os produtos com o nome da categoria).
- Um relatório com dados de duas ou mais tabelas (ex.: as vendas de um cliente, com os produtos de cada uma).
- “Quem não tem”: `LEFT JOIN` com `IS NULL` (ex.: os clientes que nunca compraram).

### Exemplo · Os aluguéis com o nome do cliente e o título do jogo

```python
def verAlugueis():
    print("LISTA DE ALUGUÉIS")

    alugueis = banco.consultar('''
        SELECT a.cod_aluguel, c.nome_cliente, j.titulo_jogo, a.data_prevista, a.data_devolucao
        FROM alugueis a
        JOIN clientes c ON c.cod_cliente = a.cod_cliente
        JOIN jogos j ON j.cod_jogo = a.cod_jogo
        ORDER BY a.cod_aluguel;
    ''')

    print("Código | Cliente | Jogo | Devolver até | Situação")
    for cod, cliente, jogo, prevista, devolucao in alugueis:
        if (devolucao is None):
            situacao = "Em aberto"
        else:
            situacao = "Devolvido"
        print(f"{cod} | {cliente} | {jogo} | {prevista:%d/%m/%Y} | {situacao}")
```

```
LISTA DE ALUGUÉIS
Código | Cliente | Jogo | Devolver até | Situação
1 | Ana Lima | Corrida Turbo | 05/11/2026 | Devolvido
2 | Ana Lima | Reino Perdido | 13/11/2026 | Em aberto
3 | Ana Lima | Futebol Total | 15/11/2026 | Em aberto
4 | Ana Lima | Cidade Pixel | 17/11/2026 | Em aberto
5 | Bruno Costa | Corrida Turbo | 14/11/2026 | Devolvido
6 | Carla Dias | Reino Perdido | 18/11/2026 | Em aberto
```

Dois JOINs, um para cada FK da tabela `alugueis`. A data de devolução vazia (`NULL`) chega no Python como `None`.

---

## Etapa 6 · Pelo menos uma operação de regra de negócio

Além do CRUD, o sistema deve ter **pelo menos uma** operação inspirada numa regra do seu negócio: o sistema **decide**, **calcula** ou **impede** alguma coisa. A regra pode ser uma opção nova do menu ou fazer parte de uma operação do CRUD, como no exemplo abaixo. Explique no `README.md` qual é a regra, por que ela existe e como testar.

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

### Exemplo · Limite de 3 aluguéis em aberto (opção 23)

A regra fica dentro do cadastro de aluguel: antes do `INSERT`, o sistema consulta os aluguéis em aberto do cliente.

```python
def cadastrarAluguel():
    print("NOVO ALUGUEL")

    verClientes()
    cod_cliente = int(input("Digite o código do cliente: "))

    # Regra de negócio: no máximo 3 aluguéis em aberto por cliente
    em_aberto = banco.consultar('''
        SELECT cod_aluguel FROM alugueis
        WHERE cod_cliente = %s AND data_devolucao IS NULL;
    ''', (cod_cliente,))

    if (len(em_aberto) >= 3):
        print("Este cliente já tem 3 aluguéis em aberto. Ele precisa devolver um jogo antes.")
        return

    verJogos()
    cod_jogo = int(input("Digite o código do jogo: "))
    dias = int(input("Quantos dias de aluguel? "))

    try:
        banco.manipular('''
            INSERT INTO alugueis
            VALUES (default, %s, %s, default, CURRENT_DATE + %s, NULL);
        ''', (cod_cliente, cod_jogo, dias))
        print("ALUGUEL REGISTRADO!")
    except Exception as error:
        print("ERRO AO REGISTRAR ALUGUEL")
```

Três testes, com os dados iniciais do `setup.py`:

| Teste | O que acontece |
|-------|----------------|
| Cliente 1, a Ana | `Este cliente já tem 3 aluguéis em aberto. Ele precisa devolver um jogo antes.` A regra recusou, e o `INSERT` nem foi tentado. |
| Cliente 2, o Bruno · jogo 5 · 3 dias | `ALUGUEL REGISTRADO!` O aluguel aparece na opção 21, em aberto. |
| Cliente 2 · jogo 5 · −1 dia | `ERRO AO REGISTRAR ALUGUEL`: o `CHECK` `ck_aluguel_datas` recusou a data prevista antes da retirada. |

Repare na divisão de tarefas: o **Python** aplica a regra que depende de contar registros; o **banco** garante as regras que valem sempre (`CHECK`, FK, `UNIQUE`).

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

### Exemplo · `README.md` da Locadora Joystick

```markdown
# Locadora de Jogos Joystick

## O cenário
A Locadora Joystick aluga jogos de PS5, Xbox, Switch e PC. (...o briefing da Etapa 1...)

## O banco
Três tabelas: clientes, jogos e alugueis (o N:N entre clientes e jogos).
O DER e o MER estão na pasta modelagem.

## A regra de negócio
Um cliente pode ter no máximo 3 aluguéis em aberto (sem data de devolução).
Ao cadastrar um aluguel (opção 23), o sistema conta os aluguéis em aberto do cliente
e recusa o quarto. Como testar: a Ana Lima (cliente 1) já tem 3 aluguéis em aberto
nos dados iniciais.

## Como rodar
1. pip install "psycopg[binary]" python-dotenv
2. Copie o .env.exemplo com o nome .env e preencha com os dados da Aiven
3. python setup.py
4. python main.py
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
5. **Pense nos dados iniciais junto com a regra de negócio:** deixe casos em que a regra aceita e casos em que ela recusa, como a Ana do exemplo.
6. **Faça commits com frequência**, sempre conferindo o `git status`.
