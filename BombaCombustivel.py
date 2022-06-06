class BOMBACOMB:
    tanqueBomba = {"gasolina": 1, "alcool": 1, "diesel": 1}
    preco = {"gasolina": 2.50, "alcool": 2.37, "diesel": 2.58}

    def __init__(self, tipoCombustivel="g"):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = 0

        if tipoCombustivel == "g":
            print("gasolina Selecionado")
            self.tipoCombustivel = "gasolina"
            self.valorLitro = BOMBACOMB.preco["gasolina"]

        elif tipoCombustivel == "a":
            print("alcool Selecionado")
            self.tipoCombustivel = "alcool"
            self.valorLitro = BOMBACOMB.preco["alcool"]

        elif tipoCombustivel == "d":
            print("diesel Selecionado")
            self.tipoCombustivel = "diesel"
            self.valorLitro = BOMBACOMB.preco["diesel"]



    def alterar_combustivel(self):
        print("g - gasolina: R$ {}".format(BOMBACOMB.preco["gasolina"]))
        print("a - alcool: R$ {}".format(BOMBACOMB.preco["alcool"]))
        print("d - diesel: R$ {}".format(BOMBACOMB.preco["diesel"]))
        tipoCombustivel = input("Selecione o tipo desejado: ")
        self.tipoCombustivel = tipoCombustivel

    def abastercer_valor(self):
        if self.valorLitro == 0:
            print("Selecione um tipo de combustível válido")

        else:
            valor = input("\nAbastecer Valor: R$: ")
            litros = valor / self.valorLitro

            if BOMBACOMB.qtd_disponivel(self, litros):
                print("Abastecido {:.2f} litros de {}".format(litros, self.tipoCombustivel))

            else:
                print("Não há combustível dispónivel")

    def abastecer_litros(self):
        if self.valorLitro == 0:
            print("Selecione um tipo de combustível válido")

        else:
            litros = float(input("\nAbastecer Litros: "))

            if BOMBACOMB.qtd_disponivel(self, litros):
                print("{:.2f} litros de {} - Total R$ {:.2f}".format(litros,
                        self.tipoCombustivel, (litros * self.valorLitro)))

                dinheiro = float(input("Dinheiro: R$ "))
                print("Troco: R$ {:.2f} \n".format(dinheiro - (litros * self.valorLitro)))

                print("Abastecido {:.2f} litros de {}".format(litros, self.tipoCombustivel))

            else:
                print("Não há combustível dispónivel")

    def alterar_valor(self):
        print("Alterar precos combustível")
        self.alterar_combustivel()

        novo_valor = float(input("Novo valor: R$ "))
        BOMBACOMB.preco[self.tipoCombustivel] = novo_valor

        print("{} valor alterado para R$ {}".format(
            self.tipoCombustivel, BOMBACOMB.preco[self.tipoCombustivel]))


    def alterar_qtd_combustivel():
        print("gasolina: {:.2f} litros".format(BOMBACOMB.tanqueBomba["gasolina"]))
        print("Álcool: {:.2f} litros".format(BOMBACOMB.tanqueBomba["ALCOOL"]))
        print("Diesel: {:.2f} litros".format(BOMBACOMB.tanqueBomba["DIESEL"]))
        preencher = input("Preencher o Tanque? (s/n)")
        if preencher[0].lower() == "s":
            BOMBACOMB.tanqueBomba = {"gasolina": 300, "ALCOOL": 300, "DIESEL": 300}

    def qtd_disponivel(self, litros):
        if litros <= BOMBACOMB.tanqueBomba[self.tipoCombustivel]:
            BOMBACOMB.tanqueBomba[self.tipoCombustivel] -= litros
            return True

        else:
            return False



def main():
    bomba = BOMBACOMB()

def menu(bomba):
    print("1 Tipo combustível")
    print("2 Abastecer por valor")
    print("3 Abastecer por litros")
    print("4 Alterar preços")
    print("5 Preencher tanque das bombas")
    opcao = input("Selecionar opção: ")

    if opcao == "1":
        bomba.alterar_combustivel()

    elif opcao == "2":
        bomba.abastercer_valor()

    elif opcao == "3":
        bomba.abastecer_litros()

    elif opcao == "4":
        bomba.alterar_valor()

    elif opcao == "5":
        BOMBACOMB.alterar_qtd_combustivel()


    else:
        print("Selecione uma opção válida.")

    return True

main()