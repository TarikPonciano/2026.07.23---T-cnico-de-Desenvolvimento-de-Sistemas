def q1_cabecalho(titulo):

    # espaco = int((40-len(titulo))/2)
    print(f"""
{"-"*40}
{titulo.center(40)}
{"-"*40}
    """)

def q8_media_notas(n1,n2,n3,n4):
    media = (n1+n2+n3+n4)/4
    return media

def q8_verificar_situacao_aluno(nome, media):

    if media >= 7 and media <= 10:
        print(f"{nome} | {media:.1f} | Aprovado")
    elif media < 7 and media >= 4:
        print(f"{nome} | {media:.1f} | Recuperação")
    elif media < 4 and media >= 0:
        print(f"{nome} | {media:.1f} | Reprovado")
    else: 
        print("MÉDIA INVÁLIDA")


# x = 30

# def dobrar(num):
    
#     return num*2

# x_dobrado = dobrar(x)
# print(x_dobrado)

# contador = 0

# def incrementar():
#     global contador
#     contador += 1

# incrementar()
# incrementar()
# incrementar()
# print(contador)
