# Crie uma agenda telefonica onde o telefone da pessoa deve ser acessado pelo seu nome. Você deve usar um dicionário onde a chave será o nome e o valor será o telefone. Peça para que a pessoa escreva um nome e mostre na tela o telefone da pessoa escolhida. Faça pelo menos 10 contatos.


agenda = {
    "Julia": "8599664433",
    "Marcos": "8598764532",
    "Lopes": "8588745423"
}
nome = input("Digite o nome da pessoa que você deseja visualizar o telefone: ")

if nome in agenda:  
    print(agenda[nome])
else:
    print("Nome não encontrado!")