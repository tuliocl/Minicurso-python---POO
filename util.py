class util:
    def Cast(option):
        try:
            aux_int = int(option)
            return aux_int
        except:
            return -1
    
    def Cast_float(number):
        try:
            aux = float(number)
            return aux
        except:
            print("ERRO AO CONVERTER")
            print("Alterar valor depois :)")
            return 0.0
