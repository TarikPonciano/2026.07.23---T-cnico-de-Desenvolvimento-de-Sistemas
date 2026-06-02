# Atividade — Funções em Python
**Técnico em Desenvolvimento de Sistemas**

---

## Nível 1 — Declaração e Chamada

**Questão 1**

Você vai criar uma função que exibe um cabeçalho formatado no terminal — útil para organizar a saída de qualquer sistema.

**O que fazer:**

1. Declare uma função chamada `cabecalho` que receba um parâmetro chamado `titulo`.
2. Dentro da função, exiba:
   - Uma linha com 40 caracteres `-`
   - O título recebido centralizado (use o método `.center(40)`)
   - Outra linha com 40 caracteres `-`
3. Fora da função, chame `cabecalho` três vezes com os títulos `"CADASTRO DE CLIENTES"`, `"RELATÓRIO DE VENDAS"` e `"CONFIGURAÇÕES"`.

**Saída esperada para `cabecalho("CADASTRO DE CLIENTES")`:**
```
----------------------------------------
          CADASTRO DE CLIENTES
----------------------------------------
```

---

**Questão 2**

Você vai criar uma função que exibe a tabuada de qualquer número — o mesmo código servirá para qualquer valor que for passado.

**O que fazer:**

1. Declare uma função chamada `tabuada` que receba um parâmetro chamado `numero`.
2. Dentro da função, use um laço `for` de `1` a `10` para calcular e exibir cada linha da tabuada no formato: `5 x  1 =  5` (alinhe os números usando f-string com largura fixa, ex: `{i:2d}` e `{resultado:3d}`).
3. Fora da função, chame `tabuada(5)` e depois `tabuada(7)`, separando as duas saídas com uma linha em branco.

**Saída esperada para `tabuada(5)`:**
```
5 x  1 =  5
5 x  2 = 10
5 x  3 = 15
5 x  4 = 20
5 x  5 = 25
5 x  6 = 30
5 x  7 = 35
5 x  8 = 40
5 x  9 = 45
5 x 10 = 50
```

---

## Nível 2 — Parâmetros

**Questão 3**

Uma academia precisa de um programa que calcule e exiba o IMC de seus alunos. Cada chamada da função representa um aluno diferente.

**O que fazer:**

1. Declare uma função chamada `calcular_imc` que receba três parâmetros: `nome`, `peso` (em kg) e `altura` (em metros).
2. Dentro da função, calcule o IMC usando a fórmula `IMC = peso / altura²` e exiba o resultado com duas casas decimais.
3. Fora da função, chame `calcular_imc` três vezes com os dados abaixo:

| Nome    | Peso (kg) | Altura (m) |
|---------|-----------|------------|
| Ana     | 62        | 1.65       |
| Carlos  | 90        | 1.80       |
| Beatriz | 55        | 1.58       |

**Saída esperada para Ana:**
```
Aluno: Ana
IMC: 22.77
```

---

**Questão 4**

Um sistema de vendas precisa imprimir os itens de uma nota fiscal. Cada produto deve ser exibido com seu preço unitário, quantidade e subtotal calculado.

**O que fazer:**

1. Declare uma função chamada `exibir_produto` que receba três parâmetros: `nome`, `preco` (valor unitário) e `quantidade`.
2. Dentro da função, calcule o subtotal (`preco * quantidade`) e exiba as informações no formato abaixo.
3. Fora da função, chame `exibir_produto` com os três produtos:
   - `"Notebook"`, `3500.00`, `2`
   - `"Mouse"`, `89.90`, `3`
   - `"Teclado"`, `149.00`, `1`

**Saída esperada para o Notebook:**
```
Produto : Notebook
Preço   : R$ 3500.00
Qtd     : 2x
Subtotal: R$ 7000.00
```

---

## Nível 3 — Valor Padrão

**Questão 5**

Uma loja quer aplicar descontos variados em seus produtos. Quando nenhum desconto for informado, o sistema deve usar 10% automaticamente.

**O que fazer:**

1. Declare uma função chamada `aplicar_desconto` com dois parâmetros: `preco` e `desconto` com valor padrão `10`.
2. Dentro da função, calcule o valor do desconto (`preco * desconto / 100`) e o preço final (`preco - valor_desconto`). Exiba os três valores formatados com duas casas decimais.
3. Fora da função, faça exatamente estas três chamadas:
   - `aplicar_desconto(200.00)` — deve usar o desconto padrão de 10%
   - `aplicar_desconto(200.00, 5)` — desconto de 5%
   - `aplicar_desconto(200.00, desconto=20)` — desconto de 20% usando argumento nomeado

**Saída esperada para `aplicar_desconto(200.00)`:**
```
Preço original : R$ 200.00
Desconto (10%) : R$ 20.00
Preço final    : R$ 180.00
```

---

**Questão 6**

Uma pizzaria quer registrar pedidos com diferentes personalizações. Quando o cliente não especifica tamanho ou borda, o sistema deve usar os valores padrão.

**O que fazer:**

1. Declare uma função chamada `registrar_pedido` com três parâmetros: `sabor` (obrigatório), `tamanho` com padrão `"média"` e `borda` com padrão `"simples"`.
2. Dentro da função, exiba um resumo do pedido com os três campos.
3. Fora da função, faça exatamente estas quatro chamadas:
   - `registrar_pedido("Calabresa")` — só o sabor, usa os dois padrões
   - `registrar_pedido("Frango", "grande")` — sabor e tamanho posicionais, borda padrão
   - `registrar_pedido("Portuguesa", "família", "catupiry")` — tudo posicional
   - `registrar_pedido("Margherita", borda="cheddar")` — sabor posicional, borda nomeada, tamanho padrão

**Saída esperada para `registrar_pedido("Calabresa")`:**
```
---- Pedido registrado ----
Sabor  : Calabresa
Tamanho: média
Borda  : simples
```

---

## Nível 4 — Return

**Questão 7**

Um caixa de mercado precisa calcular o troco do cliente. O resultado deve ser retornado pela função — não apenas impresso — para que o programa possa usá-lo depois.

**O que fazer:**

1. Declare uma função chamada `calcular_troco` com dois parâmetros: `total` (valor da compra) e `pago` (valor entregue pelo cliente).
2. Dentro da função:
   - Se `pago` for menor que `total`, exiba `"Erro: valor pago insuficiente."` e **retorne** `0`.
   - Caso contrário, **retorne** o valor do troco (`pago - total`). Não use `print` para o troco dentro da função.
3. Fora da função, chame `calcular_troco` duas vezes, armazene cada resultado em uma variável e exiba-os com `print`:
   - `calcular_troco(47.50, 50.00)` → troco válido
   - `calcular_troco(80.00, 60.00)` → pagamento insuficiente

**Saída esperada:**
```
Troco: R$ 2.50
Erro: valor pago insuficiente.
Troco: R$ 0.00
```

---

**Questão 8**

Um professor precisa de um programa que calcule a média de cada aluno e informe automaticamente sua situação. A função de média deve apenas calcular e retornar — a decisão sobre a situação fica fora dela.

**O que fazer:**

1. Declare uma função chamada `calcular_media` que receba quatro parâmetros: `n1`, `n2`, `n3`, `n4`. A função deve **retornar** a média aritmética. Não use `print` dentro dela.
2. Fora da função, chame `calcular_media` três vezes, armazene o resultado retornado em uma variável chamada `media` e, a partir dela, decida e exiba a situação do aluno usando `if/elif/else`:
   - Média ≥ 7.0 → `"Aprovado"`
   - Média ≥ 5.0 → `"Recuperação"`
   - Média < 5.0 → `"Reprovado"`
3. Use estes dados de teste:

| Aluno   | N1  | N2  | N3  | N4  |
|---------|-----|-----|-----|-----|
| Lucas   | 8.0 | 7.5 | 9.0 | 8.5 |
| Marina  | 5.0 | 6.0 | 4.5 | 5.5 |
| Pedro   | 3.0 | 4.0 | 2.5 | 3.5 |

**Saída esperada:**
```
Lucas  | Média: 8.25 | Aprovado
Marina | Média: 5.25 | Recuperação
Pedro  | Média: 3.25 | Reprovado
```

---

## Nível 5 — Escopo

**Questão 9**

Leia o código abaixo com atenção e responda as três perguntas **sem executar o programa**. O objetivo é entender o que acontece com variáveis de mesmo nome em escopos diferentes.

```python
x = 10

def dobrar():
    x = 20
    print(x)

dobrar()
print(x)
```

**Responda:**

a) Escreva exatamente o que será impresso no terminal, linha por linha. Justifique cada linha com base no conceito de escopo.

b) A linha `x = 20` dentro de `dobrar()` altera o valor do `x` que está fora da função? Explique por quê.

c) Reescreva a função `dobrar` de forma correta: ela deve receber um número por parâmetro, calcular o dobro e **retornar** o resultado. Fora da função, chame-a com `x = 10` e exiba o resultado com `print`.

**Saída esperada após a reescrita:**
```
O dobro de 10 é 20
```

---

**Questão 10**

O código abaixo tem um erro que impede sua execução. Leia-o com atenção e responda as perguntas antes de corrigi-lo.

```python
contador = 0

def incrementar():
    contador += 1

incrementar()
incrementar()
incrementar()
print(contador)
```

**Responda:**

a) Execute o código e anote o erro exibido pelo Python. Pesquise ou explique com suas palavras o que significa `UnboundLocalError` e por que ele ocorre aqui.

b) Reescreva o programa **sem usar `global`**, usando parâmetro e `return`. A função `incrementar` deve receber o valor atual do contador e retornar o valor incrementado. Fora da função, chame-a três vezes e armazene o resultado de volta na variável `contador` a cada chamada.

**Saída esperada após a reescrita:**
```
3
```

---

*Técnico em Desenvolvimento de Sistemas — Funções em Python*
