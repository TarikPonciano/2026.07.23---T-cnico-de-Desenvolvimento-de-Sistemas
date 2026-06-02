# 3. Faça um programa que recebe um palpite de um usuário e verifica se esse palpite é igual ao número secreto(usar um número aleatório). Permita que o jogador tenha até 3 tentativas.
# Bônus: Faça com o que o jogo encerre assim que o jogador acertar o número secreto.
# Bônus: Faça com que o jogo imprima uma mensagem especial para quando o número de tentativas chegar ao final.
import random

tentativas = 3
numero_secreto = random.randint(0, 10)

for i in range(tentativas):
    print(f"Você tem {tentativas} tentativas!")
    palpite = int(input("Digite seu palpite de 0 a 10:"))
    tentativas -= 1

    if palpite == numero_secreto:
        print("Você acertou!")
        break
    else:
        if tentativas == 0:
            print("Você gastou todas as tentativas! Comece o jogo novamente para tentar outra vez!")
        else:
            print("Você errou!")
        
print("Fim de Jogo!")