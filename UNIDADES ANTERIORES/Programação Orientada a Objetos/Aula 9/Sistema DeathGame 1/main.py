from classJogador import Jogador

jogador1 = Jogador("Denzel", "Estudante")

jogador1.ver_ficha()

resposta = input("À sua frente você vê um gatinho fofinho e peludo. Você irá parar para fazer carinho no gato? (S/N)")

if resposta == "S":
    jogador1.testar_sobrevivencia()
else:
    print("Você ignora o gato e segue em frente...")

jogador1.ver_ficha()

resposta = input("Você encontra um pedaço de pão de forma na rua. Deseja comer? (S/N)")

if resposta == "S":

    print("O pão era encatado! Sua sobrevivência aumentou!")

    jogador1.alterar_sobrevivencia(60, "Aumentar")

else:
    print("Você ignora o pão e segue em frente!")

jogador1.ver_ficha()