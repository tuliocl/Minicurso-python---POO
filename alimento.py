from produto import produto
from datetime import date

class alimento(produto):

    def __init__(self,id,nome,preco,peso,quantidade,marca,ano,mes,dia,data_aquisicao):
        super().__init__(id,nome,preco,peso,quantidade,marca,ano,mes,dia,data_aquisicao)
        self.type = "Alimento"
    
    def dados(self, alimentos):
        print("\n"*30)
        print("ALIMENTOS: ")
        for alimento in alimentos:
            print("NOME: {}".format(alimento.nome))
            print("ID: {}".format(alimento.id))
            print("PREÇO: {}".format(alimento.preco))
            print("PESO: {}".format(alimento.peso))
            print("QUANTIDADE: {}".format(alimento.quantidade))
            print("MARCA: {}".format(alimento.marca))
            print("VALIDADE: {}".format(alimento.validade.strftime('%d/%m/%Y')))
            print()
        
        freeze = input("ENTER para continuar")

    def validade(self,alimentos):
        data_hoje = date.today()
        print("\n"*30)
        print("Os seguintes alimentos apresentam data de validade proxima: ")
        for alimento in alimentos:
            if((alimento.validade - data_hoje).days <= 30):
                print("NOME: {}".format(alimento.nome))
                print("ID: {}".format(alimento.id))
                print()
        
        freeze = input("ENTER para continuar")
    
    def remover(self,alimentos,id):
        for alimento in alimentos:
            if(alimento.id == id):
                print("Alimento {} removido.".format(alimento.nome))
                alimentos.remove(alimento)
                freeze = input("ENTER para continuar")
                return True
        
        return False
                
    def buscar(self,alimentos,id):
        for alimento in alimentos:
            if(alimento.id == id):
                alimento.Alterar_dado()
                return True
        
        return False