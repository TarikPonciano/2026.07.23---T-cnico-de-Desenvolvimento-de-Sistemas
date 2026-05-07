# 🛒 Byte Burguer — Sistema de Pedidos

**Atividade em Dupla** · Técnico em Desenvolvimento de Sistemas · Python — Listas

---

## Briefing

Você e seu colega foram contratados como desenvolvedores júnior pela lanchonete **Byte Burguer**. O dono precisa substituir o caderno de anotações por um sistema digital que registre os pedidos do dia, calcule os totais e gere um relatório no encerramento.

O sistema será construído em Python usando apenas o que vocês já aprenderam: listas, laços de repetição e funções embutidas.

### Dados iniciais — copie no início do seu código

```python
itens  = ["X-Burguer", "X-Salada", "Fritas", "Refrigerante", "Suco", "Sorvete"]
precos = [18.50,        21.00,      9.00,     6.50,           7.00,   8.00     ]
```

Observe que as duas listas são **paralelas**: o item da posição `0` de `itens` corresponde ao preço da posição `0` de `precos`, e assim por diante.

### Regras

- Proibido usar `def`
- Usar apenas listas, `for`, `while`, `enumerate()` e funções embutidas vistas em aula
- Todo bloco de código deve ter pelo menos um comentário explicando o que faz
- **Sugestão de divisão:** um aluno cuida da exibição e do `input`, o outro cuida das listas e dos cálculos

---

## Como usar `enumerate()` — exemplo de referência

O `enumerate()` percorre uma lista devolvendo, a cada volta do `for`, dois valores ao mesmo tempo: o índice do item e o item em si.

```python
frutas = ["maçã", "banana", "uva"]

for i, fruta in enumerate(frutas):
    print(f"{i} — {fruta}")
```

```
0 — maçã
1 — banana
2 — uva
```

> 💡 `i` começa em `0`, não em `1`. Para exibir numerado a partir de `1`, use `i + 1` dentro do f-string.

Com as duas listas paralelas da atividade, você pode usar `enumerate()` para percorrer os itens e acessar o preço correspondente pelo mesmo índice:

```python
for i, nome in enumerate(itens):
    print(f"{i + 1}. {nome} ........ R$ {precos[i]:.2f}")
```

> 💡 **Por que `precos[i]` funciona?** Como as duas listas são paralelas, o índice `i` aponta para o item e para o preço correspondente ao mesmo tempo. Quando `i` vale `0`, `itens[0]` é `"X-Burguer"` e `precos[0]` é `18.50`.

---

## Etapas

### Etapa 1 — Exibir o cardápio `+2 pontos`

Usando `enumerate()` e as duas listas iniciais, exiba o cardápio numerado com o nome e o preço de cada item. A saída deve ficar parecida com isso:

```
===== CARDÁPIO =====
1. X-Burguer ........ R$ 18.50
2. X-Salada ......... R$ 21.00
3. Fritas ........... R$ 9.00
...
```

> 💡 Teste essa etapa isoladamente antes de continuar. Se o cardápio aparecer correto, você está pronto para a próxima.

---

### Etapa 2 — Preparar as estruturas de dados `+2 pontos`

Antes de qualquer loop, crie as variáveis que vão acumular informações ao longo de todo o programa:

- Uma lista vazia para guardar os **nomes dos clientes** atendidos
- Uma variável numérica para acumular o **faturamento total** do dia

Além disso, crie as duas listas que vão guardar o pedido do cliente atual — uma para os nomes dos itens e outra para os preços.

> 💡 As listas do pedido atual precisam ser "resetadas" a cada novo cliente. Pense em onde no código isso deverá acontecer — você vai retornar a esse ponto nas próximas etapas.

---

### Etapa 3 — Loop de atendimento `+2 pontos`

Crie um `while` que mantém o sistema funcionando enquanto houver clientes. A cada volta, o loop deve:

1. Exibir o cardápio
2. Perguntar o nome do próximo cliente
3. Encerrar o programa se o atendente digitar `"fim"`
4. Caso contrário, cumprimentar o cliente e seguir para o pedido

> 💡 Por enquanto, no lugar do pedido, coloque apenas um `print("pedido em construção...")` para confirmar que o loop funciona antes de avançar.

---

### Etapa 4 — Loop de pedido `+2 pontos`

Dentro do loop da Etapa 3, substitua o `print()` provisório por um segundo `while` que registra os itens. A cada volta ele deve:

1. Perguntar ao cliente qual item deseja pelo número
2. Encerrar o pedido se o cliente digitar `"0"`
3. Caso contrário, adicionar o nome e o preço do item escolhido nas respectivas listas do pedido atual

> ⚠️ O cliente digita um número, mas `input()` retorna uma string. Lembre-se de converter antes de usar como índice. E atenção: o cliente vê os itens numerados a partir de `1`, mas o índice da lista começa em `0`.

---

### Etapa 5 — Resumo do pedido `+2 pontos`

Assim que o cliente digitar `"0"`, exiba um resumo com todos os itens que ele pediu e o valor total. Use `sum()` para calcular o total. A saída deve ficar parecida com isso:

```
===== PEDIDO DE ANA =====
- X-Burguer ........ R$ 18.50
- Fritas ........... R$ 9.00
- Suco ............. R$ 7.00
TOTAL: R$ 34.50
```

> 💡 Use `for` com `enumerate()` para exibir cada item com seu preço. O índice `i` te permite acessar o preço correspondente na lista de preços do pedido.

---

### Etapa 6 — Fechar o pedido e passar para o próximo `+2 pontos`

Após exibir o resumo, o programa deve:

1. Adicionar o nome do cliente à lista de clientes do dia
2. Somar o total do pedido ao faturamento acumulado do dia
3. Limpar as listas do pedido atual para receber o próximo cliente
4. Voltar ao início do loop de atendimento

> 💡 Para limpar uma lista sem criar uma nova variável, atribua uma lista vazia a ela: `lista = []`. Faça isso com as duas listas do pedido (nomes e preços) antes de iniciar o próximo atendimento.

---

### Etapa 7 — Relatório final `+2 pontos`

Quando o atendente digitar `"fim"`, exiba o relatório do dia com:

- Total de clientes atendidos, usando `len()`
- Nome de todos os clientes que passaram pela lanchonete
- Item mais caro do cardápio com seu preço, usando `max()`
- Item mais barato do cardápio com seu preço, usando `min()`
- Faturamento total do dia acumulado ao longo do programa

---

### Entrega completa `+5 pontos`

Todas as etapas funcionando de forma integrada, sem erros, com código comentado.

---

## Desafios Bônus

### Bônus 1 — Remoção de item `+2 pontos`

Antes de fechar o pedido, pergunte ao cliente se ele deseja remover algum item. Se sim, solicite o número do item a remover e use `.pop()` nas duas listas simultaneamente para manter a sincronia entre nomes e preços. Exiba o pedido atualizado antes de mostrar o total.

> ⚠️ É fundamental remover pela posição nas duas listas ao mesmo tempo. Se remover só de uma, elas ficam fora de sincronia e os preços passam a não corresponder mais aos itens corretos.

---

### Bônus 2 — Desconto por volume `+2 pontos`

Aplique um desconto de 10% no total se o pedido tiver 4 ou mais itens. Use `len()` para verificar a quantidade. Informe o valor original, o desconto aplicado e o total final no resumo do pedido.

---

### Bônus 3 — Item mais pedido do dia `+2 pontos`

Ao final do relatório, exiba qual foi o item mais pedido durante o dia. Para isso, mantenha ao longo do programa uma lista que acumula todos os itens de todos os pedidos. Ao final, percorra a lista de itens do cardápio e use `.count()` para contar quantas vezes cada um aparece. O item com a maior contagem é o mais pedido.

---

## Dica de estrutura

```
[ exibir cardápio ]
        ↓
[ loop de clientes ]        ← while até "fim"   (Etapas 3–6)
    [ loop de itens ]       ← while até "0"     (Etapa 4)
    [ resumo do pedido ]                         (Etapa 5)
    [ fechar e reiniciar ]                       (Etapa 6)
        ↓
[ relatório final ]                              (Etapa 7)
```

---

## Entrega

O projeto deve ser entregue por meio de um **repositório no GitHub** enviado para o e-mail **tarikponciano@ce.senac.br**.

### O repositório deve conter

- O arquivo `.py` com o código do projeto
- Um arquivo `README.md` com o **nome completo dos dois integrantes da dupla**

### Formato do e-mail

- **Assunto:** `Byte Burguer — [Nome do Aluno 1] e [Nome do Aluno 2]`
- **Corpo:** o link do repositório público no GitHub

> ⚠️ Repositórios privados não serão avaliados. Certifique-se de que o repositório está público antes de enviar o link.

---

## Pontuação

| | Pontos |
|---|---|
| Etapa 1 — Exibir o cardápio | 2 |
| Etapa 2 — Preparar as estruturas de dados | 2 |
| Etapa 3 — Loop de atendimento | 2 |
| Etapa 4 — Loop de pedido | 2 |
| Etapa 5 — Resumo do pedido | 2 |
| Etapa 6 — Fechar o pedido e reiniciar | 2 |
| Etapa 7 — Relatório final | 2 |
| Entrega completa | 5 |
| **Total base** | **19** |
| | |
| Bônus 1 — Remoção de item | 2 |
| Bônus 2 — Desconto por volume | 2 |
| Bônus 3 — Item mais pedido do dia | 2 |
| **Total máximo possível** | **25** |
