# Atividade — Engenharia de Requisitos
## Etapa 2: Implementação em Python e validação cruzada

Na Etapa 1, cada aluno especificou os requisitos de um sistema em um documento estruturado. Agora esse documento sai do papel: as **duplas serão formadas pelo professor**, e cada integrante vai **implementar em Python o documento do colega**.

> O documento de um vira a especificação que o outro precisa entender e construir. É aqui que se descobre se os requisitos foram escritos com clareza suficiente para alguém **de fora** conseguir implementá-los.

---

## Como funciona

A dupla **troca os documentos** da Etapa 1:

- O **Aluno A** implementa o sistema especificado no documento do **Aluno B**.
- O **Aluno B** implementa o sistema especificado no documento do **Aluno A**.

Cada um trabalha sobre a especificação do colega — **sem reescrever o documento**. Se algo estiver ambíguo ou faltando, isso deve ser **anotado** (vira material para o feedback no final), e o aluno segue registrando a **suposição** que adotou para continuar.

---

## O que implementar

O foco é **uma das funcionalidades do CRUD** descrita no documento — escolha em conjunto com o autor do documento qual será (criar, consultar, atualizar ou excluir o objeto principal). A implementação deve incluir:

- **A funcionalidade escolhida**, funcionando para o objeto principal do sistema.
- **As validações e regras de negócio** ligadas a essa funcionalidade, conforme o documento. *(Ex.: campo obrigatório não pode ficar vazio; um identificador não pode se repetir; um valor não pode ser negativo; um dado precisa seguir um formato.)*
- **Pelo menos uma classe**, definida com base nas especificações do documento. A classe deve representar o **objeto principal** do sistema, com os **atributos** vindos dos campos descritos no documento, e ser efetivamente **usada** pela funcionalidade implementada.

> Não é necessário implementar o CRUD inteiro. Vale mais **uma funcionalidade bem-feita e validada**, apoiada em uma classe coerente com o documento, do que quatro pela metade.

---

## Orientações técnicas

- Linguagem: **Python**.
- Estrutura de arquivos **plana**, no mesmo diretório:
  - um arquivo para a **classe** do objeto principal (ex.: `classProduto.py`);
  - um arquivo `main.py` que usa a classe e executa a funcionalidade.
- A **classe** deve ter os atributos que representam o objeto (com base nos campos do documento).
- A funcionalidade pode rodar via **terminal** (entrada e saída por texto) — não é preciso interface gráfica.
- Os dados podem ficar **em memória** (ex.: uma lista de objetos) durante a execução; não é exigido banco de dados.

---

## Validação cruzada e feedback

Ao final, **cada integrante valida o trabalho do outro** e registra um feedback curto, em dois pontos:

**1. Sobre o documento (Etapa 1)**

- O documento foi **claro o suficiente** para implementar sem adivinhação?
- Os requisitos estavam **completos** (faltou alguma informação)?
- Houve **ambiguidades** ou suposições que você precisou fazer?

**2. Sobre o protótipo (Etapa 2)**

- A funcionalidade implementada **corresponde** ao que o documento pedia?
- As **validações e regras de negócio** foram contempladas?
- Há algo que **melhoraria** a implementação?

> O feedback deve ser **construtivo e específico** — apontar o ponto e sugerir como melhorar, não apenas dizer se "ficou bom".

---

## O que entregar

1. O **código Python** da funcionalidade implementada — incluindo **pelo menos uma classe** (arquivo da classe + `main.py`).
2. O **link do repositório no GitHub** com o projeto.
3. O **documento da Etapa 1 usado como base** para produzir o software (o documento do colega).
4. O **registro de feedback** (os dois pontos acima), validando documento e protótipo do colega.
5. Se houver, a lista de **suposições** que você precisou adotar durante a implementação.

---

## Entrega

- **Formato:** dupla (formada pelo professor). Cada integrante entrega a sua implementação e o seu feedback.
- **Onde entregar:** pelo **Google Classroom**.
- **Arquivos:** incluir o **link do projeto no GitHub** e o **documento da Etapa 1** que serviu de base para a implementação.
- **Identificação:** incluir o **nome dos dois integrantes** e indicar **qual documento** cada um implementou.
