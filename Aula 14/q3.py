# 3. Em uma competição de corrida um programa deve receber quantos metros cada competidor correu. Execute o programa até que seja inserido 0 na quantidade de metros percorridos. Ao final mostre qual foi o maior percurso registrado.
# Bônus: Colete também o nome de cada competidor e exiba o nome do competidor com o maior percurso

maior = 0

nome_maior_corrida = ""


while True:
    nome = input("Digite o nome do competidor: ")
    distancia = float(input("Digite quantos metros foram corridos: "))

    if distancia < 0:
        print("Digite um valor positivo para distância da corrida!")
        continue

    if distancia == 0:
        print("Encerrando cadastro de percursos!")
        break


    if distancia > maior:
        maior = distancia
        nome_maior_corrida = nome
    


print(f"O maior percurso foi: {maior} metros")
print(f"O corredor foi: {nome_maior_corrida}")
