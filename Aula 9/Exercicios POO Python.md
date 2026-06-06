# Lista de Exercícios — Programação Orientada a Objetos (POO)

**Curso:** Técnico em Desenvolvimento de Sistemas — Senac
**Tema:** Classes, atributos e métodos

---

## Orientações gerais

- Cada exercício deve ser resolvido criando uma **classe**.
- Use o método `__init__` para definir os **dados (atributos)** do objeto.
- Crie **métodos** para realizar as ações pedidas.
- No final de cada exercício, **crie um objeto** da classe e **chame os métodos** para testar.
- Lembre-se de usar `self` para acessar os atributos dentro dos métodos.

---

## Exercício 1 — Pessoa

Crie uma classe `Pessoa` com os atributos `nome` e `idade`.

Crie os seguintes métodos:
- `apresentar()` — exibe na tela: `"Olá, meu nome é ... e tenho ... anos."`
- `fazer_aniversario()` — aumenta a idade em 1 ano.

> **Teste:** crie uma pessoa, mostre a apresentação, faça aniversário e apresente novamente.

---

## Exercício 2 — Retângulo

Crie uma classe `Retangulo` com os atributos `largura` e `altura`.

Crie os seguintes métodos:
- `calcular_area()` — exibe a área (largura × altura).
- `calcular_perimetro()` — exibe o perímetro (2 × largura + 2 × altura).

> **Teste:** crie um retângulo com largura 5 e altura 3 e mostre a área e o perímetro.

---

## Exercício 3 — Conta Bancária

Crie uma classe `ContaBancaria` com os atributos `titular` e `saldo`.

Crie os seguintes métodos:
- `depositar(valor)` — soma o valor ao saldo.
- `sacar(valor)` — subtrai o valor do saldo, mas só se houver saldo suficiente. Caso contrário, exiba `"Saldo insuficiente."`.
- `mostrar_saldo()` — exibe o nome do titular e o saldo atual.

> **Teste:** crie uma conta, faça um depósito, tente um saque maior que o saldo e depois um saque válido.

---

## Exercício 4 — Produto

Crie uma classe `Produto` com os atributos `nome`, `preco` e `quantidade`.

Crie os seguintes métodos:
- `valor_total()` — exibe o valor total em estoque (preço × quantidade).
- `aplicar_desconto(percentual)` — diminui o preço de acordo com o percentual informado.
- `mostrar_dados()` — exibe o nome, o preço e a quantidade do produto.

> **Teste:** crie um produto, mostre os dados, aplique um desconto de 10% e mostre os dados novamente.

---

## Exercício 5 — Carro

Crie uma classe `Carro` com os atributos `modelo`, `velocidade` (inicia em 0) e `ligado` (inicia como `False`).

Crie os seguintes métodos:
- `ligar()` — muda `ligado` para `True` e exibe `"O carro foi ligado."`.
- `acelerar(valor)` — aumenta a velocidade somente se o carro estiver ligado. Caso contrário, exiba `"Ligue o carro primeiro."`.
- `frear(valor)` — diminui a velocidade (não pode ficar negativa).
- `mostrar_velocidade()` — exibe a velocidade atual.

> **Teste:** tente acelerar com o carro desligado, ligue o carro, acelere, freie e mostre a velocidade.

---

## Exercício 6 — Aluno

Crie uma classe `Aluno` com os atributos `nome`, `nota1` e `nota2`.

Crie os seguintes métodos:
- `calcular_media()` — exibe a média das duas notas.
- `verificar_situacao()` — exibe `"Aprovado"` se a média for maior ou igual a 6, e `"Reprovado"` caso contrário.

> **Teste:** crie um aluno com notas 7 e 5, mostre a média e a situação.

---

## Exercício 7 — Lâmpada

Crie uma classe `Lampada` com o atributo `ligada` (inicia como `False`).

Crie os seguintes métodos:
- `ligar()` — muda `ligada` para `True`.
- `desligar()` — muda `ligada` para `False`.
- `estado()` — exibe `"A lâmpada está acesa."` ou `"A lâmpada está apagada."` de acordo com a situação.

> **Teste:** mostre o estado, ligue a lâmpada, mostre o estado, desligue e mostre novamente.

---

## Exercício 8 — Termômetro

Crie uma classe `Termometro` com o atributo `temperatura`.

Crie os seguintes métodos:
- `aumentar(valor)` — aumenta a temperatura.
- `diminuir(valor)` — diminui a temperatura.
- `verificar()` — exibe `"Frio"` se a temperatura for menor que 15, `"Agradável"` entre 15 e 30, e `"Quente"` acima de 30.

> **Teste:** crie um termômetro com 20 graus, verifique, aumente para 35, verifique novamente.

---

## Desafio Final — Funcionário

Crie uma classe `Funcionario` com os atributos `nome`, `salario` e `cargo`.

Crie os seguintes métodos:
- `aumentar_salario(percentual)` — aumenta o salário pelo percentual informado.
- `promover(novo_cargo)` — altera o cargo do funcionário.
- `mostrar_dados()` — exibe o nome, o cargo e o salário atual.

> **Teste:** crie um funcionário, mostre os dados, dê um aumento de 15%, promova-o para um novo cargo e mostre os dados novamente.

---

**Bom trabalho! 🚀**
