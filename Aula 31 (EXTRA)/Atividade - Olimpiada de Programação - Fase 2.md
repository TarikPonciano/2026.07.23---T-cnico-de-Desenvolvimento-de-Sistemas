# 🏆 Olimpíada de Programação — Fase 2
## Técnico em Desenvolvimento de Sistemas

---

## 📋 Visão Geral

Na Fase 2, o professor disponibilizará todas as questões criadas pelas equipes na Fase 1. Cada equipe deverá resolver o maior número possível de questões das equipes adversárias e compartilhar as soluções via GitHub.

> 💡 Quanto mais questões sua equipe resolver, mais chances de pontuar — mas atenção à qualidade: soluções mal feitas também serão avaliadas.

---

## 👥 Equipes

As equipes permanecem as mesmas da Fase 1.

---

## 🎯 O que fazer na Fase 2

- O professor disponibilizará as questões de todas as equipes
- Cada equipe deve tentar resolver **o maior número possível** de questões
- As soluções devem ser organizadas e compartilhadas via **repositório no GitHub**

---

## 📝 Como organizar as soluções

Cada solução deve ser entregue em um arquivo `.py` com o nome da equipe autora e dos integrantes da equipe resolutora como comentário no topo:

```python
# Equipe resolutora: Os Pythonistas
# Integrantes: Ana, Bruno, Carla, Diego
#
# Questão: Troco do Mercadinho
# Equipe autora: Debug Squad

preco = float(input("Preço: "))
pago = float(input("Pago: "))

if pago < preco:
    print("Valor insuficiente")
else:
    troco = pago - preco
    print(f"Troco: R$ {troco:.2f}")
```

---

## 📦 Entrega

O repositório no GitHub deve seguir a estrutura abaixo:

```
📁 [Nome da Equipe]/
├── [Equipe Adversária 1]/
│   ├── questao1.py
│   ├── questao2.py
│   └── questao3.py
├── [Equipe Adversária 2]/
│   ├── questao1.py
│   └── questao2.py
└── ...
```

O link do repositório deve ser enviado pelo **Google Classroom** conforme orientações do professor.

---

## 🏅 Critérios de Avaliação — Fase 2

| Colocação | Pontos |
|-----------|--------|
| 🥇 1º lugar | **20 pts** |
| 🥈 2º lugar | **14 pts** |
| 🥉 3º lugar | **10 pts** |

### Critério 1 — Total de Questões Resolvidas
Quantidade total de questões das equipes adversárias que a equipe conseguiu resolver corretamente.

### Critério 2 — Total de Oponentes que Resolveram sua Questão
Quanto mais equipes conseguirem resolver as questões que a sua equipe criou, mais pontos ela recebe — isso indica que os enunciados eram bem elaborados e compreensíveis.

### Critério 3 — Qualidade e Criatividade das Soluções
Avalia a clareza, organização e criatividade do código entregue. Soluções bem estruturadas, legíveis e que resolvem o problema de forma elegante serão melhor avaliadas.

### Critério 4 — Distribuição de Trabalho entre os Membros
Avalia se todos os integrantes contribuíram com a resolução das questões, observada pelo professor durante as aulas.

---

## 📊 Pontuação Total da Olimpíada

A pontuação final de cada equipe é a soma dos pontos obtidos nas duas fases:

| | Fase 1 | Fase 2 | Total Máximo |
|-|--------|--------|--------------|
| Critérios | 3 × 10 pts | 4 × 20 pts | **110 pts** |

---

## ❓ Dúvidas rápidas

**Posso resolver questões da minha própria equipe?** Não. Apenas questões das equipes adversárias contam.

**E se minha solução estiver errada?** Apenas soluções corretas são contabilizadas no Critério 1.


---

---

## 📂 Questões por Equipe

---

### 🟢 Equipe 1 — VibeCodianos

---

**Questão 1 — Simulador de Emprestimo bancario**

Maria deseja solicitar um emprestimo bancario ao Banco para o financiamento de uma casa. O banco possui regras claras para aprovar ou negar o credito bancario.

**Regra:** O emprestimo será aprovado quando a prestacao mensal não exceder 30% de seu salario.

O programa deve receber:
1. O valor da casa que será financiada pelo banco.
2. O valor do Salario da pessoa que deseja o financiamento.
3. Quantos anos de financiamento do emprestimo.

Calcule se o valor do empréstimo for maior ou menor que o salário de Maria. Se o valor da prestação exceder o limite de 30% do salário, empréstimo negado. Se o valor da prestação não exceder o limite, empréstimo aprovado.

---

**Questão 2 — Simulador de Alistamento Militar**

Joao deseja se alistar no serviço militar porém é preciso analisar sua idade.

**Regra:** O programa deve informar se já é hora de alistar ou já passou o tempo do alistamento. Deve conter o tempo que falta para se alistar ou o prazo que passou. (No Brasil, o alistamento é obrigatorio aos 18 anos de idade.)

O programa deve pedir:
1. O ano de nascimento do solicitante.

---

**Questão 3 — Simulador de um Pagamento**

O programa deve ser executado em um laço de repetição `while`.

João deseja efetuar um pagamento de uma conta, com as seguintes opções:
- 1: À vista dinheiro com 10% de desconto.
- 2: À vista no cartão com 5% de desconto.
- 3: Até 2 parcelas no cartão sem desconto.
- 4: 3 parcelas ou mais com 20% de juros do total da compra.

**Regra:** O usuário deve escolher uma dessas opções, e deve aparecer o valor final a ser calculado, dependendo da situação. Se o usuário digitar o número 0 nas opções, encerre o programa.

O programa deve pedir o preço da compra.

---

### 🔴 Equipe 2 — Expressos Vermelhos de Monty

---

**Questão 1 — Organizar os Rankings**

Durante uma competição de natação, cada participante levou um determinado tempo para concluir a prova. Quanto menor o tempo, melhor será a colocação no ranking. Os participantes foram: Aline com 3 minutos, Denzel com 2 minutos, Lay com 5 minutos e Stefano com 4 minutos.

Criar um programa que receba o nome dos participantes e o tempo que cada participante levou para concluir a prova. Organize as cronometragem em um ranking, do primeiro ao último lugar, considerando o menor tempo como a melhor colocação. Exiba o ranking final na tela.

---

**Questão 2 — Cadastro de Emprego**

Crie um programa (usando `while`) de cadastro de emprego para uma empresa de café. O programa precisa informar o nome, idade, salário, civil e sexo do funcionário. Além disso o nome precisa ter mais de 3 caracteres, a idade não pode passar de 150 anos, o salário não pode ser menos que 0 e no final exiba os dados cadastrados.

---

**Questão 3 — Lista de Compras**

Maria Chiquinha foi ao supermercado e decidiu anotar os produtos que precisava comprar. Ela quer ajuda para armazenar os nomes dos produtos em uma lista.

Criar um programa que peça ao usuário o nome dos produtos e armazene-os em uma lista. Ao final, exiba todos os produtos cadastrados na tela e a quantidade de cada um.

---

### ⚪ Equipe 3 — Nome não informado

---

**Questão 1 — Estoque de uma Farmácia**

Lucas precisa organizar o estoque de sua nova farmácia e precisa de um programa que ajude ele com esse processo.

Crie um programa de gerenciamento de estoque com as seguintes funções:
- 1. Cadastrar novo medicamento.
- 2. Vizualizar medicamentos em estoque.
- 0. Sair do sistema.

Utilize o dicionário a seguir para facilitar no teste do programa:

```python
medicamentos = [ 
    {"Nome": "Amoxicilina", "Preço": 45.90, "Quantidade em estoque": 120},
    {"Nome": "Ibuprofeno", "Preço": 18.50, "Quantidade em estoque": 85},
    {"Nome": "Paracetamol", "Preço": 12.30, "Quantidade em estoque": 200},
    {"Nome": "Dipirona Monoidratada", "Preço": 15.20, "Quantidade em estoque": 150},
    {"Nome": "Omeprazol", "Preço": 28.90, "Quantidade em estoque": 90},
    {"Nome": "Losartana Potássica", "Preço": 22.40, "Quantidade em estoque": 110},
    {"Nome": "Simvastatina", "Preço": 35.60, "Quantidade em estoque": 65},
    {"Nome": "Cloridrato de Metformina", "Preço": 19.80, "Quantidade em estoque": 140},
    {"Nome": "Cetoconazol Creme", "Preço": 24.15, "Quantidade em estoque": 40},
    {"Nome": "Azitromicina", "Preço": 33.00, "Quantidade em estoque": 75}
]
```

Exemplo de execução:
```
=== ESTOQUE DA FARMÁCIA ===
    1. Cadastrar novo medicamento no estoque.
    2. Vizualizar medicamentos em estoque.

    0. Sair do sistema.

--> 1

== Cadastro de Medicamentos ==

Digite o nome do remédio: 
Digite o preço do remédio: 
Digite quantos entrará no estoque: 

Medicamento cadastrado com sucesso!

--> 2

== Vizualisar Medicamentos em Estoque ==

(Listar os medicamentos.)
```

---

**Questão 2 — Banho de animais**

Fernando precisava de um sistema que organizasse os preços de banho dos animais.

Crie um programa que receba o nome do animal e informe o valor do serviço, declare uma lista com alguns animais.

Exemplo de execução:
```
Valores do banho dos animais
Digite o nome do animal: Gato
Gato | R$ 35.0
```

---

**Questão 3 — Descontos e Gorjetas**

Um restaurante precisa calcular um desconto de 10% em cima do valor de um cliente se caso seu consumo for acima de R$ 150. Se caso não tiver desconto informe também. Logo após calcule a gorjeta do garçom: se o valor do cliente for maior que R$ 200 o garçom recebe 10% desse valor, se for acima de R$ 300 o garçom recebe 15% do valor. Imprima a nota fiscal no final.

Exemplo 1:
```
== Restaurante ==
Digite o valor da conta do cliente: 500
 -- Nota Fiscal --
    Valor da compra: R$ 500.0
    Desconto aprovado: Desconto de 10% aprovado

    Valor Total a pagar: R$ 450.0

-----------------------------------------

-- Gorjeta do garçom --
Ganhou comissão de 10% em cima do valor total do cliente.
R$ 50.0
```

Exemplo 2:
```
== Restaurante ==
Digite o valor da conta do cliente: 50
 -- Nota Fiscal --
    Valor da compra: R$ 50.0
    Desconto aprovado: Sem desconto aprovado

    Valor Total a pagar: R$ 50.0

-----------------------------------------

-- Gorjeta do garçom --
Sem comissão.
R$ 0
```

---

*Olimpíada de Programação · Técnico em Desenvolvimento de Sistemas*
