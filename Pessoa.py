
class ContaCorrente:
    def __init__(self, tipoCombustivel,valorLitro,quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
  
    def AlterarNome(self,anos):
        anos = int(input("Quanto anos vai envelhecer: "))
        cresc = 0
        if self.idade + anos <= 21:
            cresc = anos * 0.5
        if self.idade < 21:
            if self.idade + anos > 21:
                cresc = ((21 - self.idade) * 0.5)
        self.idade += anos
            

    def AlterarNome(self):
        NovoNome = input("Qual o novo nome do correntista? ")
        self.nomedocorrentista = NovoNome
        print("O correntista se chama: {}".format(self.nomedocorrentista	))

    def Saque(self):
        print("A pessoa tem {} Kg".format(self.peso))



def main():
    contacorrente = ContaCorrente(nomedocorrentista="",numerodaconta=0,saldo=0)

    nomedocorrentista = input("Insira o nome do correntista: ")
    contacorrente.nomedocorrentista = nomedocorrentista
    numerodaconta = input("Insira o numero da conta do correntista: ")
    contacorrente.numerodaconta = numerodaconta

    pergunta = input("Deseja mudar o nome do correntista? sim ou não? ")
    if pergunta == "sim":
        contacorrente.AlterarNome()

main()