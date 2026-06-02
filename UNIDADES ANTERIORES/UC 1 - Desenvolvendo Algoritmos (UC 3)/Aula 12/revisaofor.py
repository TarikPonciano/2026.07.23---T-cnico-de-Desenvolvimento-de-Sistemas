soma = 0
contador = 0

for i in range(0,2501):
    if i % 2 == 0:
        soma += i
        contador += 1
        print(i)

print(f'''

Soma: {soma}
Contagem: {contador}
''')