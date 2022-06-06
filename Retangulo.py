
class Pessoa:
    def __init__(self, nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

  
    def Envelhecer(self,anos):
        anos = int(input("Quanto anos vai envelhecer: "))
        cresc = 0
        if self.idade + anos <= 21:
            cresc = anos * 0.5
        if self.idade < 21:
            if self.idade + anos > 21:
                cresc = ((21 - self.idade) * 0.5)
        self.idade += anos
            

    def Engordar(self):
        print("A pessoa tem {} Kg".format(self.peso))

    def Emagrecer(self):
        print("A pessoa tem {} Kg".format(self.peso))

    def Crescer(self):
        print("A pessoa tem {} metros de altura pela idade dela".format(self.altura))


def main():
    pessoa = Pessoa(nome="",idade=0,peso=0,altura=0)
    nome = input("Insira o nome da pessoa: ")
    pessoa.nome = nome
    idade = input("Insira o idade da pessoa: ")
    pessoa.idade = idade
    peso = int(input("Insira o peso da pessoa: "))
    pessoa.peso = peso
    altura = input("Insira o altura da pessoa: ")
    pessoa.altura = altura
    
    
    pessoa.Envelhecer()
    pessoa.Engordar()
    pessoa.Emagrecer()
    pessoa.Crescer()
    
main()
