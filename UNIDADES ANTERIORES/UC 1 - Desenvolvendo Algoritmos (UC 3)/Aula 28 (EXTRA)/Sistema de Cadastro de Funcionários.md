# Sistema de Cadastro de Funcionários

## Objetivo

Desenvolver um sistema de cadastro de funcionários que implementa as operações básicas de CRUD (Create, Read, Update, Delete), utilizando **funções** como estrutura fundamental do programa. O sistema deverá incluir validações de dados e um menu interativo para o usuário.

## Descrição Geral

O sistema funcionará através de um **menu de opções** onde o usuário pode:
- Criar novos funcionários
- Visualizar funcionários cadastrados
- Alterar dados de funcionários existentes
- Remover funcionários da base de dados

Os dados serão armazenados em uma **lista de dicionários**, onde cada funcionário é representado por um dicionário contendo suas informações.

---

## Estrutura de Dados

### Funcionário (Dicionário)

Cada funcionário deve ser representado como um dicionário com as seguintes chaves:

```python
{
    "nome": str,            # Nome completo
    "cpf": str,             # CPF (11 dígitos)
    "cargo": str,           # Cargo/Função
    "salario": float        # Salário mensal
}
```

**Nota:** A posição do funcionário na lista é utilizada como referência (índice 0 para o primeiro, índice 1 para o segundo, etc.)

### Lista Global de Funcionários

Manter uma lista global que armazena todos os funcionários cadastrados:

```python
funcionarios = []
```

---

## Requisitos Funcionais

### 1. Menu Principal

O programa deverá exibir um menu com as seguintes opções:

```
====== SISTEMA DE CADASTRO DE FUNCIONÁRIOS ======
1. Criar Funcionário
2. Ver Funcionários
3. Alterar Funcionário
4. Remover Funcionário
5. Sair
===============================================
Digite sua opção:
```

### 2. Funções Obrigatórias

#### 2.1 Funções de CRUD

**`criar_funcionario()`**
- Solicita dados do usuário (nome, CPF, cargo, salário)
- Valida os dados usando as funções de validação
- Adiciona o funcionário à lista como um novo elemento
- Exibe mensagem de sucesso

**`ver_funcionarios()`**
- Verifica se existe funcionários cadastrados
- Se vazio, exibe mensagem apropriada
- Se houver dados, exibe todos em formato legível (tabela ou listagem)
- Mostra a posição (índice), Nome, CPF, Cargo e Salário
- A posição começa do 0 (primeiro funcionário) ou do 1 (conforme preferência didática)

**`alterar_funcionario()`**
- Solicita a posição do funcionário a alterar (índice na lista)
- Valida se a posição existe na lista
- Se não encontrado, exibe mensagem de erro
- Se encontrado, permite alterar qualquer campo
- Valida os novos dados
- Atualiza o funcionário na lista

**`remover_funcionario()`**
- Solicita a posição do funcionário a remover (índice na lista)
- Valida se a posição existe na lista
- Solicita confirmação antes de remover
- Remove o funcionário da lista
- Exibe mensagem de confirmação

#### 2.2 Funções Utilitárias de Validação

**`validar_cpf(cpf)`**
- Recebe o CPF como string
- Verifica se contém exatamente 11 dígitos
- Retorna `True` se válido, `False` caso contrário
- Exemplo: "12345678901" é válido

**`validar_salario(salario)`**
- Recebe o salário como entrada do usuário
- Verifica se pode ser convertido para número (float)
- Verifica se o valor é maior que 0
- Retorna `True` se válido, `False` caso contrário
- Exemplo: "1500.50" é válido, "-100" é inválido


### 3. Fluxo do Programa

1. Exibir menu
2. Ler opção do usuário
3. Chamar a função correspondente
4. Retornar ao menu (loop contínuo até opção "Sair")

---

## Critérios de Aceitação

- [ ] O programa possui um menu interativo que se repete até o usuário escolher sair
- [ ] Todas as 5 funções de CRUD/Menu estão implementadas
- [ ] As 2 funções de validação (CPF e Salário) funcionam corretamente
- [ ] Não é possível cadastrar funcionários com dados inválidos
- [ ] Cada funcionário é acessado pela sua posição (índice) na lista
- [ ] É possível visualizar todos os funcionários cadastrados com suas posições
- [ ] É possível alterar qualquer dado de um funcionário existente usando sua posição
- [ ] É possível remover um funcionário com confirmação usando sua posição
- [ ] O programa exibe mensagens claras ao usuário em todas as operações
- [ ] Tratamento de erros (entrada inválida, posição não encontrada, etc.)

---

## Exemplos de Uso

### Exemplo 1: Criar Funcionário

```
Opção: 1
Nome: João Silva
CPF: 12345678901
Cargo: Desenvolvedor
Salário: 3500.00
✓ Funcionário criado com sucesso!
```

### Exemplo 2: Validação Falha

```
Opção: 1
Nome: Maria Santos
CPF: 123456789       ← Apenas 9 dígitos
✗ CPF inválido! Deve conter 11 dígitos.

Salário: -500       ← Valor negativo
✗ Salário inválido! Deve ser um número positivo.
```

### Exemplo 3: Visualizar Funcionários

```
Opção: 2
====== FUNCIONÁRIOS CADASTRADOS ======
Pos | Nome          | CPF          | Cargo         | Salário
0   | João Silva    | 12345678901  | Desenvolvedor | 3500.00
1   | Maria Santos  | 98765432100  | Designer      | 2800.00
=======================================
```

### Exemplo 4: Alterar Funcionário

```
Opção: 3
Posição do funcionário: 0
Novo cargo: Gerente de Desenvolvimento
Novo salário: 4200.00
✓ Funcionário alterado com sucesso!
```

### Exemplo 5: Remover Funcionário

```
Opção: 4
Posição do funcionário: 1
Tem certeza que deseja remover Maria Santos? (s/n): s
✓ Funcionário removido com sucesso!
```

---

## Orientações de Implementação

### Boas Práticas

1. **Separação de responsabilidades**: Cada função deve fazer uma única coisa bem
2. **Reutilização**: Use as funções de validação sempre que precisar validar dados
3. **Mensagens claras**: Informe ao usuário o que está acontecendo em cada etapa
4. **Tratamento de erros**: Sempre valide entradas antes de processar
5. **Indentação e comentários**: Código legível e bem documentado

### Estrutura Sugerida do Código

```python
# Variável global
funcionarios = []

# Funções de validação
def validar_cpf(cpf):
    # implementar

def validar_salario(salario):
    # implementar

# Funções de CRUD
def criar_funcionario():
    # implementar

def ver_funcionarios():
    # implementar

def alterar_funcionario():
    # implementar

def remover_funcionario():
    # implementar

# Função principal (menu)
def menu_principal():
    # implementar

# Chamar função principal
menu_principal()
```


