from util import util
from alimento import alimento
from bebida import bebida
from limpeza import limpeza
from datetime import date

class funcoes:
    def adicionar_produto(self,alimentos,bebidas,limpezas,id):
        print("\n"*30)
        print("Qual o tipo do produto?")
        print("[1] - ALIMENTO")
        print("[2] - BEBIDA")
        print("[3] - LIMPEZA")
        option = input("Digite a id da opção: ")
        option_int = util.Cast(option)
       
        if(option_int != 1 and option_int != 2 and option_int != 3):
            return id#retorna a id anterior sem adicionar nada

        print("\n"*30)
        nome = input("NOME DO PRODUTO: ")

        preco = input("VALOR DO PRODUTO R$: ")
        preco_float = util.Cast_float(preco)

        peso = input("PESO KG: ")
        peso_float = util.Cast_float(peso)

        quantidade = input("QUANTIDADE: ")
        quantidade_float = util.Cast_float(quantidade)

        marca = input("MARCA: ")

        print("DADOS DE VALIDADE")
        ano = input("ANO: ")
        ano_int = util.Cast(ano)

        mes = input("MES (Número): ")
        mes_int = util.Cast(mes)

        dia = input("DIA: ")
        dia_int = util.Cast(dia)

        data_aquisicao = date.today()

        if(option_int == 1):
            novo_alimento = alimento(id,nome,preco_float,peso_float,quantidade_float,marca,ano_int,mes_int,dia_int,data_aquisicao)
            alimentos.append(novo_alimento)
       
        elif(option_int == 2):
            nova_bebida = bebida(id,nome,preco_float,peso_float,quantidade_float,marca,ano_int,mes_int,dia_int,data_aquisicao)
            bebidas.append(nova_bebida)
            
        elif(option_int == 3):
            novo_limpeza = limpeza(id,nome,preco_float,peso_float,quantidade_float,marca,ano_int,mes_int,dia_int,data_aquisicao)
            limpezas.append(novo_limpeza)
        
        id += 1
        return id
    
    def Remover_produto(self,alimentos,bebidas,limpezas):
        print("\n"*30)
        aux = input("Indique a ID do produto: ")
        id = util.Cast(aux)
        
        flag = False

        flag = alimento.remover(self,alimentos,id)
        if(flag == True):
            return

        flag = bebida.remover(self,bebidas,id)
        if(flag == True):
            return

        flag = limpeza.remover(self,limpezas,id)
        
        if(flag == False):
            print("Produto não encontrado")
            freeze = input("ENTER para continuar")

    def Alterar_dados(self,alimentos,bebidas,limpezas):
        flag = False
       
        print("\n"*30)
        aux = input("Indique a ID do produto: ")
        id = util.Cast(aux)

        flag = alimento.buscar(self,alimentos,id)
        if(flag == True):
            return

        flag = bebida.buscar(self,bebidas,id)
        if(flag == True):
            return

        flag = limpeza.buscar(self,bebidas,id)

        if(flag == False):
            print("Produto não encontrado")
            reeze = input("ENTER para continuar")


    def Relatorio_de_informacoes(self,alimentos,bebidas,limpezas):

        print("\n"*30)
        print("Qual o tipo do produto que deseja listar?")
        print("[1] - ALIMENTO")
        print("[2] - BEBIDA")
        print("[3] - LIMPEZA")
        option = input("Digite a id da opção: ")
        option_int = util.Cast(option)

        if(option_int == 1):
            alimento.dados(self,alimentos)

        elif(option_int == 2):
            bebida.dados(self,bebidas)

        elif(option_int == 3):
            limpeza.dados(self,limpezas)

    def Relatorio_de_validade(self,alimentos,bebidas,limpezas):
        alimento.validade(self,alimentos)
        bebida.validade(self,bebidas)
        limpeza.validade(self,limpezas)
