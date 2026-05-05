# 23. Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.

numero = int(input("Digite um número inteiro: "))
operacoes = 0

for n in range(1, numero+1):
    primo = True

    for i in range(2, (n//2) + 1):
        operacoes += 1
        if n % i == 0:
            primo = False
            break
    
    if primo == True:
        print(f"{n} é primo!")
    else:
        print(f"{n} não é primo!")


print(f"FORAM USADAS {operacoes} operações")