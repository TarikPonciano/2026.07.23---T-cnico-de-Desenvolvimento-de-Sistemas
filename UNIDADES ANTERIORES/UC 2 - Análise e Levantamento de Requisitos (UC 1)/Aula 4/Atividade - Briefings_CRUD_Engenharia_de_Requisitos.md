# Atividade — Engenharia de Requisitos
## Etapa 1: Especificação e documentação de requisitos

Cada aluno receberá, por sorteio, um dos seis briefings deste documento. O briefing é a **fala de um cliente**: ele descreve o problema e o que precisa, mas **não entrega os requisitos prontos**. Seu trabalho é ler com atenção, interpretar e **especificar os requisitos** em um documento estruturado.

> Esta é a **primeira etapa** da atividade, voltada apenas à **documentação**. Em uma etapa seguinte, uma das funcionalidades descritas será implementada em Python — por isso, ao especificar, pense em **operações simples sobre um cadastro** (criar, consultar, atualizar e excluir um registro).

---

## O que entregar

Um **documento estruturado** contendo as seções abaixo.

### 1. Introdução

Apresente o projeto: qual é o sistema, para quem é, qual problema resolve e qual é o **objeto principal** que ele gerencia (aquilo que será cadastrado e mantido). Use o briefing como base.

### 2. Requisitos Funcionais

O que o sistema **deve fazer**. Como o sistema é um cadastro, os requisitos funcionais giram em torno das quatro operações sobre o objeto principal:

- **Criar** um novo registro.
- **Consultar / listar** registros (incluindo busca por algum campo).
- **Atualizar** os dados de um registro existente.
- **Excluir** um registro.

Inclua também qualquer outra função que o texto do cliente exigir.

### 3. Requisitos Não-Funcionais

Atributos de **qualidade** do sistema: validação de campos obrigatórios, tempo de resposta, facilidade de uso, formato esperado dos dados, etc.

### 4. Regras de Negócio

Restrições e políticas do **domínio**, derivadas do que o cliente descreveu. Exemplos do tipo que pode aparecer: um campo que não pode se repetir, um valor que não pode ser negativo, um formato obrigatório para certo dado.

---

## Modelo para descrição dos requisitos

**Adote um modelo padrão** para descrever cada requisito — isso deixa o documento consistente e mais fácil de ler. Sugestão de modelo:

| Campo | Descrição |
|---|---|
| **Código** | Identificador único (ex.: RF01, RNF01, RN01). |
| **Nome** | Título curto do requisito. |
| **Prioridade** | Alta, Média ou Baixa. |
| **Descrição** | O que o requisito estabelece, de forma clara e objetiva. |
| **Entradas** | Dados que o sistema recebe para atender o requisito. |
| **Saídas** | Resultado esperado após a execução. |

**Exemplo preenchido** (sistema de cadastro de livros):

| Campo | Conteúdo |
|---|---|
| **Código** | RF01 |
| **Nome** | Cadastrar livro |
| **Prioridade** | Alta |
| **Descrição** | O sistema deve permitir cadastrar um novo livro no acervo, informando seus dados. |
| **Entradas** | Título, autor, categoria, ISBN e quantidade de exemplares. |
| **Saídas** | Confirmação do cadastro e o livro registrado no sistema. |

---

## Lembretes

- Um requisito **não está no texto literalmente** — você precisa interpretá-lo. Na dúvida, **anote a suposição feita**.
- Mantenha os requisitos **simples e objetivos**: pense em uma operação por requisito.
- Use o **modelo de descrição** de forma consistente em todos os requisitos.

---

## Entrega

- **Formato:** atividade **individual**.
- **Onde entregar:** pelo **Google Classroom**.
- **Prazo:** **sexta-feira, 19/06**.

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
