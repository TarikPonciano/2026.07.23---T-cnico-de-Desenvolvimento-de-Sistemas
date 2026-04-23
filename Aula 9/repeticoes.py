while True:

    nota = float(input("Digite sua nota de 0 a 10:"))

    if nota >= 0 and nota <= 10:
        print("DEU CERTO")
        break
    else:
        print("Digite uma nota válida. Tente Novamente")