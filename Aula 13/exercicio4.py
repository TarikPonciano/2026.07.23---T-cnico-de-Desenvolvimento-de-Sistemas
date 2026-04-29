# 4. Uma estação de metereologia contratou você para criar um programa que calcula a média de temperatura de um dia. O seu programa deve perguntar quantas temperaturas serão inseridas, fazer a leitura dessas temperaturas e ao final informar qual foi a temperatura média daquele dia, a temperatura máxima e a temperatura mínima do dia.
# Bônus: Exiba uma lista com todas as temperaturas inseridas

qtd_temperaturas = int(input("Digite quantas temperaturas serão informadas: "))

soma_temperaturas = 0

maior_temperatura = None
menor_temperatura = None

historico = ""


for i in range(qtd_temperaturas):
    temperatura = float(input("Digite uma leitura de temperatura: "))

    historico += f"{i+1}. {temperatura}°C\n"
    soma_temperaturas += temperatura

    if maior_temperatura == None:
        maior_temperatura = temperatura

    if temperatura > maior_temperatura:
        maior_temperatura = temperatura

    if menor_temperatura == None:
        menor_temperatura = temperatura

    if temperatura < menor_temperatura:
        menor_temperatura = temperatura

    

media_temperatura = soma_temperaturas / qtd_temperaturas

print("------ DADOS DO DIA ------")
print(f"Média do Dia: {media_temperatura}°C ")
print(f"Maior Temperatura: {maior_temperatura}°C ")
print(f"Menor Temperatura: {menor_temperatura}°C ")


print("-------- HISTÓRIO DE TEMPERATURAS--------")
print(historico)

