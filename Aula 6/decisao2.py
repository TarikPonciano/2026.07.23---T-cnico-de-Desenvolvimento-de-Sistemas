# 2.Receba o nome de um animal se o animal for gato imprima "Miau Miau", se o animal for cachorro imprima "Au Au", se o animal for papagaio imprima "Lôro quer biscoito" se não for nenhum dos animais imprima "Animal Não Catalogado".

animal = input("Digite a espécie do animal desejado: ")

if animal == "Gato":
    print("Miau Miau")
elif animal == "Cachorro":
    print("Au Au")
elif animal == "Papagaio":
    print("Lôro quer biscoito")
elif animal == "Tartaruga":
    print("AAAAAAANNNNNNNNN")
else:
    print("Animal Não Catalogado")