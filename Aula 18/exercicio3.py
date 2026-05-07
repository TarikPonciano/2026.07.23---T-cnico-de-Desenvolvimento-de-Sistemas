# 3. Boletim simples
# Dada a lista notas = [7.0, 5.5, 8.5, 4.0, 9.0, 6.5], exiba a maior nota, a menor nota e a média da turma usando max(), min(), sum() e len().

notas = [7.0, 5.5, 8.5, 4.0, 9.0, 6.5]

maior_nota = notas[0]

for n in notas:
    if n > maior_nota:
        maior_nota = n

print(f"Maior Nota: {maior_nota}")
print(f"Menor Nota: {min(notas)}")
media = sum(notas)/len(notas)
print(f"Média da turma: {media:.1f}")