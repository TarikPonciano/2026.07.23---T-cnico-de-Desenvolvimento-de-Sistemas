# 1. Crie um programa que pergunta se uma pessoa tem reserva para o restaurante. Verifique se a resposta foi especificamente "Sim" e imprima o resultado da verificação:

#Ex: "Entrada Permitida: {True/False}"

print("Bem vindo ao Restaurante XYZ")

resposta = input("Você já possui reserva no restaurante?(Sim/Não)")

verificar_reserva = resposta == "Sim" or resposta == "sim"

print(f"Entrada Permitida: {verificar_reserva}")