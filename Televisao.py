class Pessoa:
    def __init__(self, nome="", idade=0, peso=0, altura=0.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def crescer(self, centimentros):
        self.altura += centimentros / 100
        print("A pessoa cresceu {} cm de altura".format(centimentros))

    def engordar(self, quilos):
        self.peso += quilos
        print("A pessoa engordou {} kg".format(quilos))

    def emagrecer(self, quilos):
        self.quilos -= kg
        print("A pessoa emagreceu {} kg".format(quilos))

    def envelhecer(self, anos):
        cresc = 0

        if self.idade + anos <= 21:
            cresc = anos * 0.5

        if self.idade < 21:
            if self.idade + anos > 21:
                cresc = ((21 - self.idade) * 0.5)

        self.idade += anos

        print("A pessoa agora tem {} anos de idade.".format(self.idade))
        self.crescer(cresc)

def main():
    pessoa = Pessoa("Teste", 12, 60, 1.68)

    pergunta1 = int(input("Quanto deseja crescrer? (cm): "))
    pessoa.crescer(pergunta1)

    pergunta2 = int(input("Quanto deseja engordar? (kg): "))
    pessoa.engordar(pergunta2)

    pergunta3 = int(input("Quanto deseja emagrecer? (kg): "))
    pessoa.emagrecer(pergunta3)

    pergunta4 = int(input("Quanto deseja envelhecer? (anos): "))
    pessoa.envelhecer(pergunta4)

main()