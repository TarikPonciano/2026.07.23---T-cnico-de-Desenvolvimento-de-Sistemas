idade = int(input("Digite sua idade:"))

if idade >= 0 and idade <= 17:
    print("Você é criança 🧒")
elif idade >= 18 and idade <= 59:
    print("Você é adulto 🧑")
elif idade >= 60:
    print("Você é sênior 👴")
else:
    print("Você é alienígena 👽")

