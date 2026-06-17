# Atividade — Engenharia de Requisitos
## Briefings para Sorteio — Documentação de um CRUD simples

Cada equipe receberá, por sorteio, um dos seis briefings deste documento. O briefing é a **fala de um cliente**: ele descreve o problema e o que precisa, mas **não entrega os requisitos prontos**. O trabalho de vocês é ler com atenção, extrair os requisitos e iniciar o documento formal do sistema.

---

## O que entregar

**1. Documento formal de requisitos**

- **Introdução** — descrição breve do sistema, com base no briefing sorteado.
- **Requisitos Funcionais** — as quatro operações do CRUD (criar, consultar, atualizar, excluir) e o que mais o texto exigir.
- **Requisitos Não-Funcionais** — atributos de qualidade (validação, desempenho, usabilidade…).
- **Regras de Negócio** — restrições e políticas do domínio (ex.: campo único, sem valor negativo, formato de dado).
- **Especificação dos requisitos** — use o modelo: `Código`, `Nome`, `Prioridade`, `Descrição`, `Entradas` e `Saídas`.

**2. Modelagem de uma classe**

A partir do **objeto principal** do briefing (aquilo que o sistema cadastra e gerencia), modelem **uma classe** que o represente. A definição deve incluir:

- O **nome** da classe.
- Os **atributos**, com base nos campos que o cliente citou no briefing.
- Os **métodos** correspondentes às operações do CRUD (criar, consultar, atualizar, excluir).

> A classe deve refletir os requisitos levantados — atributos vêm dos campos do briefing, métodos vêm das funcionalidades descritas.

**3. Implementação de uma funcionalidade**

Escolham **uma das funcionalidades** descritas no briefing (um dos requisitos funcionais) e **implementem-na** em código, de forma coerente com:

- O **requisito** correspondente (o que o documento especificou).
- A **classe** modelada no item anterior.

A implementação deve demonstrar a funcionalidade funcionando para o objeto principal (por exemplo, cadastrar um item, ou buscar pelo campo de identificação).

---

## Lembretes

- Um requisito **não está no texto literalmente** — vocês precisam interpretá-lo. Na dúvida, **anotem a suposição feita**.
- O **objeto principal** do briefing é aquilo que o sistema cadastra e gerencia — é a classe principal sobre a qual o CRUD acontece.
- A funcionalidade implementada deve ser **uma das que vocês mesmos documentaram** — requisito, classe e código precisam conversar entre si.

---

## Entrega

- **Formato:** atividade em **duplas**, sorteadas em sala.
- **Onde entregar:** pelo **Google Classroom**.
- **O que incluir:** o **nome da dupla** no material entregue.
- **Prazo:** **segunda-feira, 22/06**.

---

## Referências e modelos de apoio

- **Requisitos Funcionais e Não-Funcionais** — [Modelo de Requisitos (UFU)](https://www.facom.ufu.br/~ronaldooliveira/PDS-2019-1/Aula6-ModeloRequisitos.pdf) ou [Documentos de Requisitos do Sistema (UFJF)](https://www2.ufjf.br/diavi//files/2016/07/DocumentosdeRequisitosdoSistema.pdf)
- **Regras de Negócio** — [O que são regras de negócio (Alura)](https://www.alura.com.br/artigos/o-que-sao-regras-de-negocio)

---
---

# Briefing 1 — Biblioteca Escolar Monteiro Lobato

| | |
|---|---|
| **Cliente** | Coordenação da biblioteca de uma escola de ensino médio |
| **Setor** | Educação |
| **Objeto principal** | Livro |

### O pedido do cliente

> "Somos uma biblioteca escolar com cerca de três mil exemplares. Hoje controlamos tudo num caderno e numa planilha antiga, e vivemos perdendo o rastro dos livros. Quando um aluno pergunta se temos certo título, a bibliotecária precisa procurar estante por estante."

### Situação atual

- Não sabemos, de forma rápida, quais títulos temos nem quantas cópias de cada um.
- Às vezes cadastram o mesmo livro duas vezes, com grafias diferentes.
- Quando um livro sai de circulação (danificado ou perdido), ele continua aparecendo na planilha.

### O que precisamos

> "Queremos um sistema simples onde a equipe consiga registrar cada livro do acervo, encontrar um título rapidamente quando alguém perguntar, manter as informações sempre atualizadas e retirar do sistema os livros que não fazem mais parte do acervo. As informações que consideramos importantes para cada livro são título, autor, categoria, ISBN e a quantidade de exemplares."

---
---

# Briefing 2 — Mini Mercado Bom Preço

| | |
|---|---|
| **Cliente** | Proprietário de um mercado de bairro |
| **Setor** | Varejo / Comércio |
| **Objeto principal** | Produto |

### O pedido do cliente

> "Tenho um mercadinho de bairro com umas quatrocentas mercadorias diferentes. Anoto os preços de cabeça e no papel, e isso já me deu prejuízo: vendi produto abaixo do custo e descobri tarde demais que tinha acabado o estoque de itens que vendem muito."

### Situação atual

- Não tenho controle de quanto ainda resta de cada produto na prateleira.
- Quando o fornecedor reajusta o preço, eu demoro a atualizar e me perco.
- Tenho produtos que parei de vender, mas que continuam anotados, atrapalhando a conferência.

### O que precisamos

> "Preciso de algo onde eu consiga lançar os produtos que vendo, consultar rapidamente um item pelo nome ou pela categoria, corrigir o preço e a quantidade sempre que mudar, e apagar os produtos que saíram de linha. Para cada produto eu costumo anotar nome, categoria, preço, quantidade em estoque e o código de barras."

---
---

# Briefing 3 — Agenda de Contatos · Escritório Vega

| | |
|---|---|
| **Cliente** | Secretária de um escritório de contabilidade |
| **Setor** | Serviços / Administrativo |
| **Objeto principal** | Contato |

### O pedido do cliente

> "Trabalho num escritório que fala com muita gente: clientes, fornecedores, contatos pessoais do chefe. Hoje os números estão espalhados entre celular, papéis e e-mails antigos. Quando preciso achar um telefone na hora, é um sufoco."

### Situação atual

- Os contatos estão misturados e não consigo separar o que é cliente do que é pessoal.
- Tenho telefones desatualizados e não sei qual é o certo.
- Quando alguém troca de e-mail, eu não tenho onde corrigir de forma organizada.

### O que precisamos

> "Quero uma agenda digital onde eu possa adicionar novos contatos, localizar uma pessoa pelo nome, atualizar o telefone ou o e-mail quando mudarem, e remover contatos que não uso mais. De cada contato eu gosto de guardar o nome, o telefone, o e-mail, uma categoria (pessoal ou trabalho) e a data de aniversário."

---
---

# Briefing 4 — Escola de Cursos Livres Avante

| | |
|---|---|
| **Cliente** | Secretaria de uma escola de cursos profissionalizantes |
| **Setor** | Educação |
| **Objeto principal** | Aluno |

### O pedido do cliente

> "Somos uma escola de cursos livres com várias turmas rolando ao mesmo tempo. A matrícula ainda é feita em fichas de papel. Quando um aluno tranca ou volta, a gente risca e rabisca a ficha, e fica difícil saber quem está ativo em cada curso."

### Situação atual

- Não temos uma lista confiável de quais alunos estão em cada curso.
- Quando o aluno tranca a matrícula, não há um lugar claro para registrar isso.
- Dados de contato mudam e a gente perde o histórico atualizado.

### O que precisamos

> "Gostaríamos de um sistema para matricular os alunos, listar quem está em cada curso, atualizar a situação e os dados de quem já está matriculado, e remover uma matrícula quando for o caso. Para cada aluno guardamos nome, número de matrícula, curso, e-mail, telefone e a situação atual (ativo ou trancado)."

---
---

# Briefing 5 — Equipe de Projetos · Studio Pulse

| | |
|---|---|
| **Cliente** | Líder de uma pequena equipe de criação |
| **Setor** | Produtividade / Gestão de equipe |
| **Objeto principal** | Tarefa |

### O pedido do cliente

> "Toco uma equipe pequena de cinco pessoas e a gente se organiza por bilhetinhos e mensagens soltas. O resultado é que tarefa importante se perde, e ninguém sabe ao certo o que já foi feito e o que ainda está pendente."

### Situação atual

- As tarefas ficam espalhadas e a gente esquece o que é prioritário.
- Não dá para ver de forma rápida o que já está concluído e o que está em aberto.
- Quando uma tarefa deixa de fazer sentido, ela continua poluindo a lista.

### O que precisamos

> "Queremos uma ferramenta onde a equipe possa criar tarefas, ver a lista filtrando pelo que está pendente ou pela prioridade, editar uma tarefa e marcá-la como concluída, e excluir as que não valem mais. Cada tarefa deveria ter um título, uma descrição, uma prioridade (alta, média ou baixa), um prazo e um status (pendente ou concluída)."

---
---

# Briefing 6 — Estacionamento Centro Park

| | |
|---|---|
| **Cliente** | Gerente de um estacionamento rotativo |
| **Setor** | Serviços / Mobilidade |
| **Objeto principal** | Veículo |

### O pedido do cliente

> "Administro um estacionamento no centro com bastante giro de carros e motos durante o dia. O controle de entrada e saída é feito em fichas de papel, e na hora do movimento isso trava a fila e gera confusão sobre quem entrou e a que horas."

### Situação atual

- Não conseguimos localizar rapidamente um veículo pela placa.
- Os registros de entrada se perdem e fica difícil calcular o tempo de permanência.
- Quando o carro vai embora, a ficha continua aberta por descuido.

### O que precisamos

> "Precisamos de um sistema para registrar a entrada de cada veículo, consultar um veículo pela placa, atualizar os dados quando houver erro de digitação, e dar baixa quando o veículo sai. De cada veículo registramos a placa, o modelo, a cor, o tipo (carro ou moto) e o horário de entrada."
