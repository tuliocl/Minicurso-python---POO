from produto import produto
from datetime import date

class limpeza(produto):
    
    def __init__(self,id,nome,preco,peso,quantidade,marca,ano,mes,dia,data_aquisicao):
        super().__init__(id,nome,preco,peso,quantidade,marca,ano,mes,dia,data_aquisicao)
        self.type = "Limpeza"

    def dados(self, limpezas):
        print("\n"*30)
        print("LIMPEZA: ")
        for limpeza in limpezas:
            print("NOME: {}".format(limpeza.nome))
            print("ID: {}".format(limpeza.id))
            print("PREÇO: {}".format(limpeza.preco))
            print("PESO: {}".format(limpeza.peso))
            print("QUANTIDADE: {}".format(limpeza.quantidade))
            print("MARCA: {}".format(limpeza.marca))
            print("VALIDADE: {}".format(limpeza.validade.strftime('%d/%m/%Y')))
            print()
        
        freeze = input("ENTER para continuar")

    def validade(self,limpezas):
        data_hoje = date.today()
        print("\n"*30)
        print("Os seguintes produtos de limpeza apresentam data de validade proxima: ")

        for limpeza in limpezas:
            if((limpeza.validade - data_hoje).days <= 30):
                print("NOME: {}".format(limpeza.nome))
                print("ID: {}".format(limpeza.id))
                print()
        freeze = input("ENTER para continuar")
    
    def remover(self,limpezas,id):
        for limpeza in limpezas:
            if(limpeza.id == id):
                print("Produto de limpeza {} removido.".format(limpeza.nome))
                limpezas.remove(limpeza)
                freeze = input("ENTER para continuar")
                return True
        
        return False

    def buscar(self,limpezas,id):
        for limpeza in limpezas:
            if(limpeza.id == id):
                limpeza.Alterar_dado()
                return True
        
        return False