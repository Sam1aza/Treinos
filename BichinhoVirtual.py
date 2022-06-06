class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Retangulo:
    def __init__(self, largura, altura, pontoInicial):
        self.largura = largura
        self.altura = altura
        self.pontoInicial = pontoInicial

    def centroRetangulo(self):
        x = self.pontoInicial.x + (self.largura / 2)
        y = self.pontoInicial.y + (self.altura / 2)

        centro = Ponto(x, y)

        print("Centro:", centro)

    def __str__(self):
        return "Retângulo: largura: {} altura: {} \nInicio em x: {} e y: {} \n".format(
        self.largura, self.altura, self.pontoInicial.x, self.pontoInicial.y)


def main():
    criarRetangulo = criarRetangulo()
    print("1 Criar Retângulo")
    print("2 Ver centro")
 

    op = input("Selcione uma opção = ")

    if op == "1":
        ret = criarRetangulo()

    elif op == "2":
        ret.centroRetangulo()



def criarRetangulo():
    inicio = Ponto(0, 0)
    reta = Retangulo(5, 5, inicio)

    largura = float(input("Largura: "))
    altura = float(input("Altura: "))

    reta.largura = largura
    reta.altura = altura

    x = float(input("Eixo X: "))
    y = float(input("Eixo Y: "))

    inicio = Ponto(x, y)
    reta.pontoInicial = inicio

    return reta

main()