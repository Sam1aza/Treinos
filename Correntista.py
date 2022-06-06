class Televisao:
    def __init__(self, canal="1", volume="100"):
        self.canal = canal
        self.volume = volume

    def MudarCanal(self):
        NovoCanal = input("Mudar para CANAL: ")
        self.canal = NovoCanal=
    def MudarVolume(self):
        NovoVolume = input("Mudar para VOLUME: ")
        self.volume = NovoVolume
    def VerCanal(self):
        print("Você está no canal {} e com volume {}".format(self.canal,self.volume))



def main():
    televisao = Televisao()

    while True:
        print("1.Mudar canal")
        print("2.Mudar volume")
        print("3.Ver canal e volume")
        selec = input("Escolha:")
        if selec == "1":
            televisao.MudarCanal()
        elif selec == "2":
            televisao.MudarVolume()
        elif selec == "3":
            televisao.VerCanal()
        else:
            print("Selecione uma opção acima!")

main()