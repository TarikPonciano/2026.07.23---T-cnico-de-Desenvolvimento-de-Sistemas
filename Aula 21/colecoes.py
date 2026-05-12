meses = ("Janeiro", "Fevereiro" , "Março")

mes = input("Digite o mes atual:")

if mes in meses:
    print("Você digitou um mês que existe. Parabéns!")
else:
    print("Você digitou um mês inexistente")

print(meses[0])

for m in meses:
    print(m)

for i in range(len(meses)):
    print(f"{i+1}. {meses[i]}")





