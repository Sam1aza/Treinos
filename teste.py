
class Retangulo:
    def __init__(self, comprimento,largura):
        self.comprimento = comprimento
        self.largura = largura
  
    def ValorComp(self):
        print("O valor é {}".format(self.comprimento))
    def ValorLarg(self):
        print("O valor é {}".format(self.largura))
    def MudarComp(self):
        NovoComp = input("Mudar comprimento para: ")
        self.comprimento = NovoComp
    def MudarLarg(self):
        NovaLarg = input("Mudar largura para: ")
        self.largura = NovaLarg
    def CalcArea(self):
        print("Você irá precisar de {:.2f} m2 de piso".format(
            float(self.comprimento) * float(self.largura)))
    def CalcPerim(self):
        print("Você irá precisar de {:.2f} M de rodapés".format(
            float((self.comprimento)*2) + float(self.largura)*2))
    def CalcPisoERoda(self):
        QtdRodape = self.comprimento + self.largura
        QtdPiso = self.comprimento * self.largura

def main():
    retangulo = Retangulo(comprimento=0,largura=0)
    pergunta = input("Deseja ver o valor da largura e comprimento: sim ou não?")
    if pergunta == "sim":
        retangulo.largura()
        retangulo.comprimento()
    else:
        largura = input("Insira o valor da largura: ")
        retangulo.largura = largura
        comprimento = input("Insira o valor da comprimento: ")
        retangulo.comprimento = comprimento
        retangulo.CalcArea()
        retangulo.CalcPerim()
    
main()
