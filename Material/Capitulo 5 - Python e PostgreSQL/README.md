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
3. Rode o setup da pasta (`setup_rh.py`, `setup_cinema.py` ou `setup_loja.py`) e depois os outros programas.

O `.env` tem a sua senha e **não vai para o GitHub**: o `.gitignore` do repositório já o ignora.

## Pastas

| Pasta | O que tem |
|---|---|
| `rh/` | Exemplos da exposição: `testar_conexao.py`, `setup_rh.py`, `classBanco.py`, `consultas_rh.py` e o CRUD `main.py` (o Sistema de Funcionários da UC 1, agora com banco). |
| `cinema/` | Gabaritos das Práticas 1 a 4: `setup_cinema.py`, `consultas_cinema.py`, `cadastrar_filme.py` e `GABARITO - Praticas 2 e 4.md`. Copie o `classBanco.py` da pasta `rh` para cá. |
| `loja/` | Gabarito da prática guiada da Loja Conecta: `setup_loja.py`, `classBanco.py` (com o método `inserir`) e `main.py` (produtos, pedidos com RETURNING e transação). |
