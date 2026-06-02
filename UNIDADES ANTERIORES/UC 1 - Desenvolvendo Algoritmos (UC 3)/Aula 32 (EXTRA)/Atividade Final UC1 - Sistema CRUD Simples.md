# Atividade de Entrega da Unidade — Sistema CRUD Temático

## Modalidade

**Trabalho em duplas**

## Objetivo

Aplicar os conceitos de **funções**, **estruturas de dados** (listas e dicionários) e **operações CRUD** na construção de um sistema completo com menu interativo. A dupla deverá escolher um tema próprio e desenvolver uma aplicação inspirada nele, demonstrando autonomia e criatividade na resolução de problemas.

---

## Descrição

Durante as aulas, implementamos juntos um **Sistema de Cadastro de Funcionários** utilizando funções, menu e validações. Agora é a vez de vocês aplicarem esse conhecimento em um projeto próprio.

A dupla deverá **propor um tema** e construir um sistema CRUD inspirado nele. O tema é livre, desde que permita as quatro operações básicas de cadastro. Alguns exemplos para inspirar:

- Cadastro de Livros (biblioteca)
- Cadastro de Produtos (loja/estoque)
- Cadastro de Filmes (catálogo)
- Cadastro de Alunos (escola)
- Cadastro de Receitas (culinária)
- Cadastro de Jogos (coleção)
- Cadastro de Pets (clínica veterinária)

> **Importante:** Cada tema traz características próprias que devem ser exploradas nas validações e funcionalidades extras. Pense no que faz sentido para o seu tema!

---

## Requisitos Obrigatórios

### 1. Tema Próprio

A dupla deve **propor um tema** e implementar um CRUD inspirado nele. Cada elemento do sistema deve ser representado como um **dicionário**, e o conjunto de elementos deve ser armazenado em uma **lista**.

### 2. Operações CRUD Padrão

O sistema deve implementar as quatro operações padrão, **cada uma em uma função separada**:

| Operação | Descrição |
|----------|-----------|
| **Cadastrar** | Adiciona um novo elemento à lista |
| **Ver Lista** | Exibe todos os elementos cadastrados |
| **Modificar** | Altera os dados de um elemento existente |
| **Remover** | Remove um elemento da lista |

### 3. Menu de Operação

A aplicação deve possuir um **menu interativo** que permita ao usuário escolher qual operação deseja executar. O menu deve se repetir até o usuário escolher sair.

### 4. Funções Ferramentas (mínimo 2)

A dupla deve construir **pelo menos 2 funções ferramentas (utilitárias)**. Essas funções devem servir para **validações** ou para **facilitar o processo** de programar a aplicação.

**Exemplo apresentado em aula — `validar_cpf(cpf)`:**

```python
def validar_cpf(cpf):
    # Verifica se o CPF tem exatamente 11 dígitos
    if len(cpf) == 11:
        return True
    else:
        return False
```

Outros exemplos de funções ferramentas que vocês podem criar (adapte ao seu tema):

- `validar_ano(ano)` — verifica se um ano é válido (ex: entre 1900 e 2026)
- `validar_preco(preco)` — verifica se o preço é um número maior que 0
- `validar_email(email)` — verifica se contém "@" e "."
- `formatar_titulo(texto)` — coloca a primeira letra de cada palavra em maiúscula
- `posicao_existe(posicao, lista)` — verifica se uma posição existe na lista

### 5. Funcionalidades Novas Específicas (2 obrigatórias)

A dupla deve propor **duas funcionalidades novas** como opções do menu, relacionadas ao **tema escolhido**. Essas funcionalidades devem ir além do CRUD básico e fazer sentido para o contexto.

**Exemplos por tema:**

- **Biblioteca:** "Buscar livro por autor" / "Listar apenas livros disponíveis"
- **Loja:** "Calcular valor total do estoque" / "Listar produtos abaixo do preço X"
- **Filmes:** "Listar filmes por gênero" / "Mostrar filme mais bem avaliado"
- **Escola:** "Calcular média da turma" / "Listar alunos aprovados"

---

## Estrutura Sugerida

```python
# Lista que armazena os elementos
elementos = []

# ---- Funções Ferramentas ----
def validar_exemplo(dado):
    # implementar

def ferramenta_dois(dado):
    # implementar

# ---- Operações CRUD ----
def cadastrar():
    # implementar

def ver_lista():
    # implementar

def modificar():
    # implementar

def remover():
    # implementar

# ---- Funcionalidades Específicas do Tema ----
def funcionalidade_um():
    # implementar

def funcionalidade_dois():
    # implementar

# ---- Menu Principal ----
def menu_principal():
    # implementar

# Chamar a aplicação
menu_principal()
```

---

## Checklist de Requisitos

Antes de entregar, confira se o trabalho atende a todos os pontos:

- [ ] A dupla propôs um tema próprio
- [ ] Cada elemento é representado por um dicionário, armazenado em uma lista
- [ ] A operação **Cadastrar** está implementada em uma função separada
- [ ] A operação **Ver Lista** está implementada em uma função separada
- [ ] A operação **Modificar** está implementada em uma função separada
- [ ] A operação **Remover** está implementada em uma função separada
- [ ] A aplicação possui um menu de operação que se repete
- [ ] Foram criadas pelo menos **2 funções ferramentas** (validação ou utilidade)
- [ ] Foram criadas **2 funcionalidades novas** específicas do tema, como opções do menu
- [ ] O código está organizado, comentado e funciona sem erros

---

## Dicas

1. **Comecem pelo tema:** definam bem o que vão cadastrar e quais campos cada elemento terá.
2. **Reaproveitem o que vimos em aula:** a lógica é a mesma do sistema de funcionários.
3. **Pensem nas validações certas:** o que faz sentido validar no seu tema?
4. **Sejam criativos nas funcionalidades extras:** é aí que o trabalho de vocês ganha personalidade.
5. **Testem cada função separadamente** antes de juntar tudo no menu.
