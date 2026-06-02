# Crie um programa que contém um número secreto à sua escolha (guarde 0 a 10 em uma variável) e peça ao usuário que dê um palpite (0 a 10). Imprima na tela se o usuário acertou ou errou o seu palpite.

# Bônus 1: Melhore o programa para quando o usuário errar imprima se o número secreto é maior ou menor que o palpite

# Bônus 2: Permita que o usuário tente 3 vezes antes de encerrar o programa

# Bônus 3: Faça com que o número secreto seja aleatório

import random

num_secreto = random.randint(0,100)

palpite = int(input("Digite um número de 0 a 100:"))

if palpite == num_secreto:
    print(f"Você acertou! O número secreto era: {num_secreto}")
else:
    print("Você errou!")

    if (num_secreto > palpite):
        print(f"O número secreto é maior que o seu palpite. Seu palpite foi: {palpite}")
    else:
        print(f"O número secreto é menor que o seu palpite. Seu palpite foi: {palpite}")

    palpite = int(input("Digite o seu novo palpite: "))

    if palpite == num_secreto:
        print(f"Você acertou! O número secreto era: {num_secreto}. Você acertou na segunda tentativa!")
    else:
        print("Você errou sua segunda tentativa! Só resta uma.")

        if (num_secreto > palpite):
            print(f"O número secreto é maior que o seu palpite. Seu palpite foi: {palpite}")
        else:
            print(f"O número secreto é menor que o seu palpite. Seu palpite foi: {palpite}")

        palpite = int(input("Digite o seu último palpite: "))

        if palpite == num_secreto:
            print(f"Você acertou na última chance. O número secreto era: {num_secreto}")
        else:
            print("Você errou na última chance")
            if (num_secreto > palpite):
                print(f"O número secreto é maior que o seu palpite. Seu palpite foi: {palpite}")
            else:
                print(f"O número secreto é menor que o seu palpite. Seu palpite foi: {palpite}")

            print(f"TENTATIVAS ACABARAM. O número secreto era: {num_secreto}")



            



