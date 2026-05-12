# CRUD

# Create (Inserir)

produto = {
}
produto["Nome"] = input("Digite o nome do produto: ")
produto["Preço"] = float(input("Digite o preço do produto:"))

# Read

print(produto)

print(produto["Nome"])

# print(produto.get("Estoque", "Chave não encontrada"))

# Update

produto["Nome"] = "Cereja"

produto["Preço"] = 10

print(produto)
# Delete

#produto.clear() #Remove todos os elementos do dicionário

del produto["Nome"]
# produto.pop("Nome","Chave não encontrada para remoção")

print(produto)