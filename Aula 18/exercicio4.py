# 4. Fatiamento de ranking
# Uma competição registrou os tempos (em segundos) dos 8 participantes em ordem de chegada: [12.3, 13.1, 13.8, 14.0, 14.5, 15.2, 16.0, 17.4]. Usando slicing, exiba apenas o pódio (os 3 primeiros), os 3 últimos colocados e os participantes do meio (posições 3 a 5).

tempos_de_chegada = [12.3, 13.1, 13.8, 14.0, 14.5, 15.2, 16.0, 17.4, 18.0]

print(f"Pódio: {tempos_de_chegada[0:3]}")

print(f"Últimos: {tempos_de_chegada[len(tempos_de_chegada)-3:len(tempos_de_chegada)]}")

print(f"Meio: {tempos_de_chegada[3:5]}")


# for tempo in tempos_de_chegada[0:3]:
#     print(tempo)