# 1. Lista de compras
# Crie uma lista com 5 itens de supermercado. Exiba o primeiro item, o último e o total de itens da lista usando len().

# 2. Fila de atendimento
# Uma clínica tem uma fila com os nomes: ["Carlos", "Beatriz", "Fábio", "Juliana", "Rafael"]. Adicione "Tatiane" ao final da fila e remova "Fábio" porque ele desistiu. Exiba a fila atualizada e o total de pessoas.

# 3. Boletim simples
# Dada a lista notas = [7.0, 5.5, 8.5, 4.0, 9.0, 6.5], exiba a maior nota, a menor nota e a média da turma usando max(), min(), sum() e len().

# 4. Fatiamento de ranking
# Uma competição registrou os tempos (em segundos) dos 8 participantes em ordem de chegada: [12.3, 13.1, 13.8, 14.0, 14.5, 15.2, 16.0, 17.4]. Usando slicing, exiba apenas o pódio (os 3 primeiros), os 3 últimos colocados e os participantes do meio (posições 3 a 5).

# 5. Verificação de estoque
# Um mercadinho tem a lista estoque = ["arroz", "feijão", "macarrão", "leite", "óleo"]. Peça ao usuário um produto com input() e informe se ele está ou não disponível no estoque. Depois, exiba o estoque em ordem alfabética usando sorted().

# 6. Controle de presença
# Uma turma tem 6 alunos. Use um for com enumerate() para percorrer a lista de nomes e perguntar ao usuário "presente" ou "ausente" para cada um. Ao final, exiba quantos alunos estiveram presentes e quantos faltaram.

# 7. Placar de campeonato
# Duas listas paralelas armazenam os times e seus pontos:
# times = ["Corinthians", "Palmeiras", "Santos", "São Paulo"]
# pontos = [58, 65, 42, 51]
# Use for com enumerate() para exibir a tabela de classificação. Depois encontre e exiba o time com mais pontos (localizando o índice do valor máximo com .index(max(...))).

# 8. Filtro de temperatura
# Uma estação meteorológica coletou as temperaturas diárias de um mês (30 valores entre 18°C e 38°C — o aluno pode criar a lista manualmente ou com valores inventados). Use um for para contar quantos dias ficaram acima de 30°C, calcule a média geral e exiba os dias mais quentes usando fatiamento após ordenar a lista com sorted().

# 9. Gestão de senhas de banco
# Um banco emite senhas numéricas sequenciais. Simule uma fila com 10 senhas: fila = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]. A cada iteração de um while, remova a primeira senha da fila com .pop(0), exiba "Chamando senha: XXX" e encerre quando a fila estiver vazia. Ao final, informe quantas senhas foram atendidas.

# 10. Ranking de vendas com múltiplas operações
# Uma loja registrou o nome e o total de vendas de 5 vendedores em duas listas paralelas. O aluno deve: (a) exibir o ranking completo; (b) encontrar o melhor vendedor pelo maior valor; (c) calcular a média de vendas da equipe; (d) exibir apenas os vendedores acima da média; (e) verificar se algum vendedor atingiu a meta de R$ 5.000 usando any(). Todo o processamento deve usar for, enumerate() e as funções max(), min(), sum() e len().