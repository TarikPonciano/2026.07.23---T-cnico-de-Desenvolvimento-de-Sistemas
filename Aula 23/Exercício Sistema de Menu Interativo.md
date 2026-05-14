# Atividade Prática — Sistema de Gerenciamento com Menu Interativo
**Técnico em Desenvolvimento de Sistemas — Programação em Python**

---

## Descrição

Cada grupo receberá um tema sorteado. Com base nele, vocês devem construir um sistema em Python que gerencie um cadastro de registros usando dicionários e listas, com um menu interativo em loop.

---

## O que o sistema deve ter

1. Uma lista vazia criada antes do menu para armazenar os registros
2. Um dicionário com no mínimo 5 campos para representar cada registro — os campos devem fazer sentido com o tema
3. Um menu em loop `while True` com as seguintes opções:
   - **Cadastrar** — ler os dados do usuário, montar o dicionário e adicionar à lista
   - **Listar todos** — exibir todos os registros de forma numerada
   - **Ver detalhes** — mostrar todos os campos de um registro específico escolhido pelo número
   - **Sair** — encerrar o programa
4. A **funcionalidade extra** do tema sorteado, implementada como mais uma opção no menu

---

## Requisitos técnicos

- Arquivo único `.py`
- Sem usar `def` — toda a lógica no corpo do programa
- Loop `while True` com `break` para o menu
- `if / elif / else` para as opções
- Mensagens claras para o usuário em cada operação
- O programa deve rodar sem erros

---

## Entrega

Apresentar o programa funcionando ao professor, demonstrando todas as opções do menu.

---

## Temas e Funcionalidades Extras

---

### 1 — 🐾 Clínica Veterinária
**Atributos:** nome do pet, espécie, raça, idade, nome do tutor

**Funcionalidade extra:** listar apenas os pets de uma espécie digitada pelo usuário

---

### 2 — 📚 Biblioteca
**Atributos:** título, autor, ano de publicação, gênero, ISBN

**Funcionalidade extra:** listar livros filtrando por gênero escolhido pelo usuário

---

### 3 — 🍕 Cardápio de Restaurante
**Atributos:** nome do prato, categoria, preço, tempo de preparo (min), descrição

**Funcionalidade extra:** exibir o prato mais barato e o mais caro do cardápio

---

### 4 — 🏋️ Academia
**Atributos:** nome do aluno, modalidade, horário, número de matrícula, plano (mensal/trimestral/anual)

**Funcionalidade extra:** contar quantos alunos estão cadastrados em cada modalidade

---

### 5 — 🎮 Loja de Games
**Atributos:** título, plataforma, gênero, preço, classificação etária

**Funcionalidade extra:** listar jogos filtrando por plataforma digitada pelo usuário

---

### 6 — 🌱 Estoque de Hortifruti
**Atributos:** produto, unidade (kg/unidade), quantidade em estoque, preço, fornecedor

**Funcionalidade extra:** alertar quais produtos estão abaixo de uma quantidade mínima informada pelo usuário

---

### 7 — 🚗 Locadora de Veículos
**Atributos:** modelo, marca, ano, placa, valor da diária (R$)

**Funcionalidade extra:** calcular o custo total de uma locação com base no número de dias informado pelo usuário

---

### 8 — 🏨 Hotel
**Atributos:** nome do hóspede, número do quarto, data de check-in, data de check-out, tipo de quarto (standard/luxo/suíte)

**Funcionalidade extra:** calcular o total a pagar com base na diferença de dias entre check-in e check-out e no valor da diária

---

### 9 — 💊 Farmácia
**Atributos:** nome do medicamento, laboratório, dosagem, preço, quantidade em estoque

**Funcionalidade extra:** buscar medicamentos cujo nome contenha um trecho digitado pelo usuário

---

### 10 — 🎓 Escola de Cursos Livres
**Atributos:** nome do aluno, curso, turno, data de início, situação (ativo/concluído)

**Funcionalidade extra:** listar apenas os alunos com situação "ativo"
