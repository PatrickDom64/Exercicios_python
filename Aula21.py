import os 
os.system('cls')

class Carro:
    velMax = 0
    ligado = False
    cor = ""

    def __init__(self,v,l,c):
        self.velMax = v
        self.ligado = l
        self.cor = c
    def mostrar(self):
        print("Velocidade Maxima:",self.velMax ,"Km/h")
        estado = "Sim" if self.ligado else "Não"
        print("Está ligado:",estado)
        print("Cor:",self.cor)
        print("======================================")
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False        

c1 = Carro(100,True,"Preto")
c2 = Carro(200,True,"Branco")
c3 = Carro(0,False,"Verde")

c3.ligar()

c1.mostrar()
c2.mostrar()
c3.mostrar()