# Atividade: Programação em Pares — Revisão de Python

**Curso:** Técnico em Desenvolvimento de Sistemas — Senac
**Duração estimada:** 1 hora
**Modalidade:** Duplas (pair programming)

---

## Instruções Gerais

1. Trabalhem **em dupla**: um escreve o código ("piloto"), o outro acompanha, revisa e sugere ("navegador"). Troquem os papéis a cada exercício.
2. Leiam o enunciado com atenção antes de começar a digitar.
3. Testem o código com **diferentes entradas** para garantir que funciona em todos os casos.
4. Comentem o código quando acharem necessário — bons comentários fazem parte do trabalho.
5. Caso fiquem travados por mais de 5 minutos, chamem o professor. Não gastem tempo demais em um único exercício.
6. Ao terminar, revisem juntos: o código está legível? Funciona nos casos extremos?

---

## Entrega

- Um único arquivo `.py` com todos os exercícios separados por comentários (`# Exercício 1`, `# Exercício 2`, etc.)
- Nome do arquivo: `pares_NomeAluno1_NomeAluno2.py`
- Envie pelo repositório da turma até o prazo combinado.

---

## Exercícios

### Exercício 1 — Conversor de unidades *(Tipos, operadores e formatação)*

Peça ao usuário uma **temperatura em Celsius** e converta para **Fahrenheit** e **Kelvin** usando as fórmulas:

- Fahrenheit: `F = C * 9/5 + 32`
- Kelvin: `K = C + 273.15`

Exiba os três valores com **duas casas decimais**, bem formatados. Em seguida, peça uma **distância em quilômetros** e converta para milhas (`1 km = 0.6214 mi`), também com duas casas decimais.

> **Desafio:** exiba uma mensagem diferente se a temperatura em Celsius for abaixo de 0° ("Temperatura negativa — abaixo do ponto de congelamento.").

---

### Exercício 2 — Validação de senha *(Condicionais encadeadas)*

Peça ao usuário que crie uma senha. Valide se ela atende a **todos** os critérios abaixo e informe quais estão sendo descumpridos:

- Ter pelo menos 8 caracteres
- Não pode ser igual ao nome do usuário (peça o nome também)
- Não pode conter espaços

Se todos os critérios forem atendidos, exiba `"Senha válida!"`. Caso contrário, liste cada problema encontrado.

> **Dica:** `len()` retorna o tamanho de uma string; `" " in senha` verifica se há espaço.

---

### Exercício 3 — Classificador de triângulos *(Condicionais com lógica combinada)*

Leia os três lados de um triângulo (valores decimais). Primeiro, verifique se os lados formam um triângulo válido — a soma de quaisquer dois lados deve ser maior que o terceiro. Se não for válido, informe o erro.

Se for válido, classifique quanto aos **lados**:
- Equilátero (todos iguais)
- Isósceles (dois iguais)
- Escaleno (todos diferentes)

---

### Exercício 4 — Calculadora de IMC *(Condicionais com múltiplos critérios)*

Leia o peso (kg) e a altura (m) do usuário. Calcule o IMC (`peso / altura²`) e classifique conforme a tabela:

| IMC | Classificação |
|---|---|
| Abaixo de 18,5 | Abaixo do peso |
| 18,5 a 24,9 | Peso normal |
| 25,0 a 29,9 | Sobrepeso |
| 30,0 ou mais | Obesidade |

Exiba o valor calculado com **duas casas decimais** e a classificação correspondente.

---

### Exercício 5 — Contador de dígitos e soma *(Repetição com `for` e strings)*

Peça ao usuário que digite um número inteiro positivo. Usando um laço `for` sobre os caracteres da string, calcule e exiba:

- A **quantidade de dígitos** do número
- A **soma de todos os dígitos**
- O **maior dígito** encontrado

Exemplo para a entrada `3847`:
```
Quantidade de dígitos: 4
Soma dos dígitos: 22
Maior dígito: 8
```

> **Dica:** converta o número para string com `str()` para iterar sobre os dígitos. Não vale usar `len()` diretamente para contar — use o laço.

---

### Exercício 6 — Adivinhe o número *(Repetição com `while`)*

O programa deve escolher um número fixo (pode ser definido diretamente no código, ex: `42`). O usuário tenta adivinhar. A cada tentativa, informe se o número secreto é **maior** ou **menor** do que o chute. O jogo termina quando o usuário acertar, exibindo quantas tentativas foram necessárias.

---

### Exercício 7 — Notas da turma *(Listas)*

Crie uma lista vazia. Peça ao usuário para digitar **5 notas** de alunos (use um laço `for`). Ao final, exiba:

- A **maior** nota
- A **menor** nota
- A **média** da turma
- Quantos alunos foram **aprovados** (nota ≥ 6)

---

### Exercício 8 — Filtrando a lista *(Listas e condicionais)*

Dada a lista abaixo:

```python
numeros = [4, 17, 3, 22, 9, 11, 6, 30, 1, 14]
```

Sem modificar a lista original, crie e exiba:

- Uma nova lista com apenas os números **pares**
- Uma nova lista com apenas os números **maiores que 10**

---

### Exercício 9 — Cadastro com dicionário *(Dicionários)*

Crie um dicionário que represente o cadastro de um produto com as chaves: `nome`, `categoria`, `preco` e `estoque`. Preencha com dados digitados pelo usuário. Em seguida, exiba todas as informações do produto de forma organizada.

Depois, simule a venda de uma unidade: atualize o estoque subtraindo 1 e exiba o estoque atualizado.

---

### Exercício 10 — Placar de jogadores *(Listas de dicionários + repetição)*

Crie um programa que gerencie o placar de um jogo. O programa deve:

1. Iniciar com uma lista vazia chamada `jogadores`.
2. Pedir ao usuário quantos jogadores vão participar e, para cada um, cadastrar um dicionário com `nome` e `pontos` (começando em `0`).
3. Entrar em um laço onde, a cada rodada, o usuário digita o **nome de um jogador** e a **pontuação obtida naquela rodada** — esse valor é somado aos pontos existentes. O laço continua até o usuário digitar `"fim"` no lugar do nome.
4. Ao encerrar, exibir o placar final e destacar o vencedor.

Exemplo de saída:

```
=== PLACAR FINAL ===
1º Carlos — 47 pontos
2º Beatriz — 35 pontos
3º André — 28 pontos

Vencedor: Carlos!
```


---

## Bônus — Sistema de biblioteca *(Dicionários + listas + repetição)*

### Parte A — Montando o acervo

Crie uma lista chamada `acervo` com **três dicionários** já definidos no código. Cada dicionário representa um livro com as chaves `titulo`, `autor` e `disponivel` (booleano — `True` se disponível).

Em seguida, use um laço `for` para exibir todos os livros no seguinte formato:

```
"Dom Casmurro" - Machado de Assis — Disponível
"1984" - George Orwell — Emprestado
```

> **Dica:** use um `if` dentro do `for` para escolher entre exibir "Disponível" ou "Emprestado" com base no valor do booleano.

---

### Parte B — Adicionando e buscando

Partindo do `acervo` do exercício anterior, faça duas coisas:

1. Peça ao usuário os dados de um novo livro (`titulo`, `autor`) e adicione-o ao acervo com `disponivel` igual a `True`.
2. Peça ao usuário um título e **busque** esse livro no acervo. Se encontrar, exiba as informações completas. Se não encontrar, informe que o livro não está cadastrado.

---

### Parte C — Empréstimo e devolução

Ainda usando o mesmo acervo, implemente as duas operações abaixo — cada uma lendo o título digitado pelo usuário:

- **Emprestar:** encontra o livro e muda `disponivel` para `False`. Se o livro já estiver emprestado, exiba um aviso.
- **Devolver:** encontra o livro e muda `disponivel` para `True`. Se o livro já estiver disponível, exiba um aviso.

Teste emprestando um livro, tentando emprestar de novo, e depois devolvendo.

---

### Parte D — Juntando tudo com um menu

Agora una tudo em um único programa com menu. O sistema deve iniciar com os três livros já cadastrados e oferecer as opções em loop:

- `1` — Adicionar novo livro
- `2` — Listar todos os livros
- `3` — Buscar livro pelo título
- `4` — Emprestar livro
- `5` — Devolver livro
- `0` — Sair

O programa só encerra quando o usuário escolher `0`. Opções inválidas devem exibir uma mensagem de aviso sem encerrar o programa.

---

## Bônus — Desafio extra *(para quem terminar antes)*

Adicione ao sistema do Exercício 10d a opção `6` para **listar apenas os livros disponíveis** e a opção `7` para **listar apenas os emprestados**. Em cada caso, se a lista estiver vazia, exiba uma mensagem adequada.

---

*Bom trabalho em dupla! Programar junto é uma habilidade profissional valiosa.*
