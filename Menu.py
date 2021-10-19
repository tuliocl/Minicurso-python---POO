from alimento import alimento
from bebida import bebida
from limpeza import limpeza

from funcoes import funcoes
from util import util

class Menu:

    def __init__(self):
        self.id = 0
        self.alimentos = []
        self.bebidas = []
        self.limpezas = []
        self.gerenciar = funcoes()

    def Start(self):  #apresenta o menu e espera uma resposta válida  
    
        Menu.functions()
            
        option = input("Digite a id da opção: ")
        option_int = util.Cast(option)#tenta fazer o cast pra int

        if(option_int == 1):
            self.id = self.gerenciar.adicionar_produto(self.alimentos,self.bebidas,self.limpezas,self.id)
        elif(option_int == 2):
            self.gerenciar.Remover_produto(self.alimentos,self.bebidas,self.limpezas)              
        elif(option_int == 3):  
            self.gerenciar.Alterar_dados(self.alimentos,self.bebidas,self.limpezas)      
        elif(option_int == 4):
            self.gerenciar.Relatorio_de_informacoes(self.alimentos,self.bebidas,self.limpezas) 
        elif(option_int == 5): 
            self.gerenciar.Relatorio_de_validade(self.alimentos,self.bebidas,self.limpezas)
        else:
            print("Opção invalída")
            reeze = input("ENTER para continuar")

    def functions():

        print("\n"*30)
        print("Bem vindo ao sistema do mercadinho da dona Kátia :)")
        print("[1] - ADICIONAR PRODUTO")
        print("[2] - REMOVER PRODUTO")    
        print("[3] - ALTERAR DADOS")    
        print("[4] - RELATÓRIO DE INFORMAÇÕES")
        print("[5] - RELATÓRIO DE VALIDADE")
