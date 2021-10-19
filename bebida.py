from produto import produto
from datetime import date

class bebida(produto):

    def __init__(self,id,nome,preco,peso,quantidade,marca,ano,mes,dia,data_aquisicao):
        super().__init__(id,nome,preco,peso,quantidade,marca,ano,mes,dia,data_aquisicao)
        self.type = "Bebida"

    def dados(self, bebidas):
        print("\n"*30)
        print("BEBIDAS: ")
        for bebida in bebidas:
            print("NOME: {}".format(bebida.nome))
            print("ID: {}".format(bebida.id))
            print("PREÇO: {}".format(bebida.preco))
            print("PESO: {}".format(bebida.peso))
            print("QUANTIDADE: {}".format(bebida.quantidade))
            print("MARCA: {}".format(bebida.marca))
            print("VALIDADE: {}".format(bebida.validade.strftime('%d/%m/%Y'))) 
            print()

        freeze = input("ENTER para continuar")

    def validade(self,bebidas):
        data_hoje = date.today()
        print("\n"*30)
        print("As seguintes bebidas apresentam data de validade proxima: ")
        for bebida in bebidas:
            if((bebida.validade - data_hoje).days <= 30):
                print("NOME: {}".format(bebida.nome))
                print("ID: {}".format(bebida.id))
                print()
        freeze = input("ENTER para continuar")

    def remover(self,bebidas,id):
        for bebida in bebidas:
            if(bebida.id == id):
                print("Bebida {} removido.".format(bebida.nome))
                bebidas.remove(bebida)
                freeze = input("ENTER para continuar")
                return True
        
        return False

    def buscar(self,bebidas,id):
        for bebida in bebidas:
            if(bebida.id == id):
                bebida.Alterar_dado()
                return True
        
        return False
                