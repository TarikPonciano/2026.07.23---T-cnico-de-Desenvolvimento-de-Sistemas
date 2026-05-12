# Crie uma agenda telefonica onde o telefone da pessoa deve ser acessado pelo seu nome. Você deve usar um dicionário onde a chave será o nome e o valor será o telefone. Peça para que a pessoa escreva um nome e mostre na tela o telefone da pessoa escolhida. Faça pelo menos 10 contatos.

# Utilizando a agenda do problema anterior, realize as seguintes melhorias no programa:

# 1 - Peça para o usuário o nome e telefone de 5 novas pessoas e adicione na agenda.

# 2 - Utilize um loop while para permitir que a pessoa consulte os números da agenda. O usuário deverá escrever o nome de um dos contatos e o programa deve exibir o número na tela (caso exista, senão exibir mensagem de erro) e depois pedir o nome do próximo. Continue até que a pessoa escreva o nome "Sair".
# 3 - No começo de cada repetição, exiba a lista de contatos na tela.


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