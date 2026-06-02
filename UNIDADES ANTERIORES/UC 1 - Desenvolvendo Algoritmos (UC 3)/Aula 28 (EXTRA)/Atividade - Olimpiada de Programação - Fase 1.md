# 🏆 Olimpíada de Programação
## Técnico em Desenvolvimento de Sistemas

---

## 📋 Visão Geral

A competição é dividida em duas fases:

| Fase | O que acontece |
|------|----------------|
| **Fase 1** | Cada equipe cria e resolve seus próprios enunciados |
| **Fase 2** | As equipes resolvem os enunciados das adversárias |

---

## 👥 Equipes

- Grupos de **4 integrantes**
- Cada equipe escolhe um **nome criativo** relacionado à tecnologia/programação

---

## 🎯 O que fazer na Fase 1

Cada equipe deve criar **3 questões de programação** e entregar a **solução em Python** para cada uma.

> ⚠️ Uma boa questão desafia sem ser impossível. Pense em algo que exija raciocínio lógico, mas que tenha uma solução clara.

---

## 📝 Como montar uma questão

O enunciado e a solução ficam **no mesmo arquivo `.py`**, com o enunciado escrito como comentário no topo do arquivo.

O enunciado precisa ter:

1. **Título** — nome do problema
2. **Contexto** — uma situação ou história que apresenta o desafio
3. **O que o programa deve fazer** — o que o usuário digita e o que o programa imprime
4. **Exemplos** — ao menos 2 casos com entrada e saída esperada

---

## 💡 Exemplo de bom enunciado

```python
# =============================================
# Título: Troco do Mercadinho
#
# Contexto:
# Joãozinho trabalha no caixa de um mercadinho
# e sempre se atrapalha na hora de dar o troco.
# Ajude-o criando um programa que calcule
# automaticamente o troco do cliente.
#
# O programa recebe o preço do produto e o valor
# que o cliente pagou, e deve mostrar o troco.
# Se o cliente pagou menos do que o preço,
# exiba: "Valor insuficiente"
#
# Exemplo 1:
#   Entrada:
#     Preço: 3.50
#     Pago:  5.00
#   Saída:
#     Troco: R$ 1.50
#
# Exemplo 2:
#   Entrada:
#     Preço: 8.00
#     Pago:  6.00
#   Saída:
#     Valor insuficiente
# =============================================

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

O arquivo deve ser um `.zip` com o nome da equipe e enviado pelo **Google Classroom**. Dentro do `.zip`:

```
📁 [Nome da Equipe]/
├── questao1.py    → Enunciado (comentário) + solução
├── questao2.py
└── questao3.py
```

O nome da equipe e de todos os integrantes devem aparecer como comentário no topo de **cada arquivo `.py`**, antes do enunciado:

```python
# Equipe: Os Pythonistas
# Integrantes: Ana, Bruno, Carla, Diego
#
# =============================================
# Título: Troco do Mercadinho
# ...
```

---

## 🏅 Critérios de Avaliação — Fase 1

| Colocação | Pontos |
|-----------|--------|
| 🥇 1º lugar | **10 pts** |
| 🥈 2º lugar | **7 pts** |
| 🥉 3º lugar | **5 pts** |

### Critério 1 — Qualidade do Enunciado
Clareza, narrativa envolvente, exemplos bem construídos e coerência com a solução.

### Critério 2 — Criatividade do Nome da Equipe
Originalidade, relação com tecnologia/programação e impacto.

### Critério 3 — Participação dos Membros
Envolvimento e contribuição de todos os 4 integrantes durante a Fase 1.


## ❓ Dúvidas rápidas

**Posso usar referências da internet?** Sim, mas o enunciado deve ser o mais original possível. Adaptar uma ideia é permitido; copiar um enunciado pronto, não.

**A solução precisa funcionar?** Sim. O código deve rodar e produzir as saídas dos exemplos corretamente.

**Quantos pontos posso ganhar na Fase 1?** No máximo **30 pontos** (10 por critério).

---

*Olimpíada de Programação · Técnico em Desenvolvimento de Sistemas*
