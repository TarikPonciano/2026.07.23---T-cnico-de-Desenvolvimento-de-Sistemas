#Revisão 5: Crie um programa que recebe as 5 notas de uma escola de samba e exiba na tela a média dessas 5 notas:

nota1 = float(input("Digite a nota 1:"))
nota2 = float(input("Digite a nota 2:"))
nota3 = float(input("Digite a nota 3:"))
nota4 = float(input("Digite a nota 4:"))
nota5 = float(input("Digite a nota 5:"))

media = (nota1 + nota2 + nota3 + nota4 + nota5)/5

print(f"A média da escola de samba é: {media:.1f}")