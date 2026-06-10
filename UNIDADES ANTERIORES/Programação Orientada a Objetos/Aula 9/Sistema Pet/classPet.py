class Pet():
    def __init__(self, nome, idade, especie, genero, raca="SRD"):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.raca = raca
        self.genero = genero
    def ver_ficha_pet(self):
        print(f"""
Nome: {self.nome}
Idade: {self.idade} anos
Faixa Etária: {self.verificar_faixa_etaria()}
Espécie: {self.especie}
Raça: {self.raca}
Gênero: {self.genero}
""")
    
    def verificar_faixa_etaria(self):

        if self.especie == "Cachorro" or self.especie == "Gato":
            if self.idade >= 2:
                return "Adulto"
            else:
                return "Filhote"
        else:
            if self.idade >= 1:
                return "Adulto"
            else:
                return "Filhote"
            
    def alterar_especie(self, nova_especie):

        if nova_especie in ["Cachorro", "Gato", "Calango", "Passarim"]:
            self.especie = nova_especie
            print("Espécie alterada com sucesso!")
        else:
            print("Não foi possível alterar a espécie. Espécie não catalogada!")
