class Macaco:

    def __init__(self, nome):
        self.nome = nome
        self.barriga = []



    def Comer(self, objeto):
        self.barriga.append(objeto)

    def VerBarriga(self):
        print("A barriga tem: ")
        for i in self.barriga:
            print(i)

    def digerir(self):
        self.VerBarriga()
        self.barriga = []

alimentos = ["Banana", "Laranja", "Abacaxi"]        

def exibeMenu(macacos):
    print("1 Criar macaco")
    print("2 Ver macacos")
    print("3 Sair ")
    selec = input("Selecione = ")
    print()

    if selec == "1":
        nome = input("Escolha um nome para o macaco: ")
        novo_macaco = Macaco(nome)

    elif selec == "2":
        macacos = menuMacacos(macacos)

    elif selec == "3":
        return

    return menu, macacos

def menuMacacos(macacos):

    for i in range(len(macacos)):
        print("{} - {}".format(i+1, macacos[i].nome))

    selec = input("Selecione um macaco ou pressione Enter para sair =")
    if selec.isdigit():
        selec = int(selec)
        selec = selec -1
    else:
        return macacos

    while True:
        print("\nMACACO: {}".format(macacos[selec].nome))
        print("1 Comer")
        print("2 Ver barriga")
        print("3 Digerir")
        print("4 Sair")
        opcao = input("Selecione")

        if opcao == "1":
            exibeAlimentos()
            n = int(input("Selecione a comida: "))
            n = n - 1
            macacos[selec].Comer(alimentos[n])

        elif opcao == "2":
            macacos[selec].VerBarriga()

        elif opcao == "3":
            macacos[selec].digerir()

        elif opcao == "4":
            break

    return macacos

def exibeAlimentos():
    print()
    for i in range(len(alimentos)):
        print("{} - {}".format(i+1, alimentos[i]))

macacos = []
menu = True

while menu:
    menu, macacos = exibeMenu(macacos)
