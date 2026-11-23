# Capítulo 5 · Python e PostgreSQL

Programas do Capítulo 5: o Python conversando com o PostgreSQL na Aiven, com psycopg 3 e `.env`.

## Preparar o computador (uma vez)

No terminal do VS Code:

```
pip install -r requirements.txt
```

Ou, sem o arquivo: `pip install "psycopg[binary]" python-dotenv`.

## Preparar cada projeto

1. Crie o banco na Aiven (pgAdmin → Databases → Create → Database): `rh`, `cinema` ou `loja`.
2. Na pasta do projeto, copie o `.env.exemplo` com o nome `.env` e preencha com os dados da Aiven
   (console.aiven.io → seu serviço → Overview → Connection information).
3. Rode o setup da pasta e depois os outros programas.

O `.env` tem a sua senha e **não vai para o GitHub**: o `.gitignore` do repositório já o ignora.

## As etapas do capítulo

| Etapa | Sistema RH (exposição) · `rh/` | Cinema Estrela (práticas) · `cinema/` |
|---|---|---|
| 1 · Setup | `setup_rh.py` | `setup_cinema.py` (Prática 1) |
| 2 · Primeiro sistema, sem classe | `sistema_rh.py` | `sistema_cinema.py` (Prática 2), com `consultarBanco` e `manipularBanco` |
| 3 · Classe e CRUD | `classBanco.py` e `main.py` | `classBanco.py` e `main.py` (Prática 3) |

O `setup_cinema.py` e o `sistema_cinema.py` usam o mesmo `.env` do RH, com `dbname="cinema"` no `connect`.
O CRUD da Prática 3 usa a classe, que lê o `DB_NAME`: o `.env` dessa pasta tem `DB_NAME=cinema`.

Para saber: `rh/testar_erros.py` mostra um `except` para cada tipo de erro do psycopg.

## Prática guiada · Loja Conecta · `loja/`

| Arquivo | O que tem |
|---|---|
| `setup_loja.py` | O banco do Capítulo 4, com os códigos gerados pelo banco (`START WITH` mantém os mesmos números). |
| `classBanco.py` | A classe do RH com o método `registrarVenda`: o pedido (com `RETURNING`) e os itens numa transação só. |
| `main.py` | Requisito 1: CRUD completo de produtos. Requisito 2: fluxo de venda e detalhes da venda. |
