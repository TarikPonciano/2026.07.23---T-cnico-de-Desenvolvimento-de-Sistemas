# 7. Placar de campeonato
# Duas listas paralelas armazenam os times e seus pontos:
# times = ["Corinthians", "Palmeiras", "Santos", "São Paulo"]
# pontos = [58, 65, 42, 51]
# Use for com enumerate() para exibir a tabela de classificação. Depois encontre e exiba o time com mais pontos (localizando o índice do valor máximo com .index(max(...))).

times = ["Corinthians", "Palmeiras", "Santos", "São Paulo"]
pontos = [58, 65, 42, 51]

maior_time = ""
maior_pontuacao = 0

for i in range(len(times)):
    print(times[i], pontos[i])

    if pontos[i] > maior_pontuacao:
        maior_pontuacao = pontos[i]
        maior_time = times[i]

print(f"Time com maior pontuação: {maior_time} - {maior_pontuacao} pontos")

# print(f"Time com mais pontos: {times[pontos.index(max(pontos))]} - {max(pontos)}")

# for time, ponto in zip(times, pontos):

#     print(time, ponto)