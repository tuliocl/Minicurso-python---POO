from datetime import date
from util import util

class produto:
    def __init__(self,id,nome,peso,preco,quantidade,marca,ano,mes,dia,data_aquisicao):
        
        self.id = id

        self.nome = nome  
        self.peso = peso
        self.preco = preco
        self.quantidade = quantidade
        self.marca = marca
        self.validade = date(ano, mes, dia)
        self.data_aquisicao = data_aquisicao



            

    def Alterar_dado(self):
        print("\n"*30)
        print("[1] - ALTERAR NOME")
        print("[2] - ALTERAR PESO")
        print("[3] - ALTERAR PREÇO")
        print("[4] - ALTERAR QUANTIDADE")
        print("[5] - ALTERAR MARCA")
        print("[6] - ALTERAR DATA DE VALIDADE")

        aux = input("Indique a opção: ")
        id = util.Cast(aux)

        if(id == 1):
            self.Set_nome()
        elif(id == 2):
            self.Set_peso()
        elif(id == 3):
            self.Set_preco()
        elif(id == 4):
            self.Set_quantidade()
        elif(id == 5):
            self.Set_marca()
        elif(id == 6):
            self.Set_validade()

    def Set_nome(self):
        novo_nome = input("NOVO NOME: ")
        self.nome = novo_nome

    def Set_peso(self):
        novo_peso = input("NOVO PESO: ")
        aux = util.Cast_float(novo_peso)
        self.peso = aux

    def Set_preco(self):
        novo_preco = input("NOVO PRECO: ")
        aux = util.Cast_float(novo_preco)
        self.preco = aux

    def Set_quantidade(self):
        novo_quantidade = input("NOVO QUANTIDADE: ")
        aux = util.Cast_float(novo_quantidade)
        self.quantidade = aux

    def Set_marca(self):
        nova_marca = input("NOVA MARCA: ")
        self.marca = nova_marca

    def Set_validade(self):
        novo_ano = int(input("NOVO ANO: "))
        novo_mes = int(input("NOVO MES: "))
        novo_dia = int(input("NOVO DIA: "))
        self.validade = date(novo_ano,novo_mes,novo_dia)