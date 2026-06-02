qtd_notas = int(input("Digite quantas notas serão avaliadas:"))

soma = 0

for i in range(qtd_notas):

    while True:
        nota = float(input("Digite uma nota entre 0 e 10: "))

        if nota < 0 or nota > 10:
            print("Nota inválida")       
        else:
            soma+= nota
            break


media = soma/qtd_notas

print(media)