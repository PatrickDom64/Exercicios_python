import os 
os.system('cls')


class NPC : #classe pai/base
    def __init__(self,nome,time,forca,municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    def info(self):
        print("Nome:",self.nome)
        print("Time:",self.time)
        print("Força:",self.forca)
        print("Munição:",self.municao)
        print("Vivo:",("sim" if self.vivo else "não"))
        print("Energia:",self.energia)
        print("----------------------------")

class Soldado(NPC):
    def __init__(self,nome,time):
        self.forca = 200
        self.municao = 200
        super().__init__(nome,time,self.forca,self.municao)
        def inf(self):
            super().info()


s1 = Guarda("Olho Vivo",1)
s2 = Ninja("Super Atento",1)
s3 = Soldado("Tiro certo",1)
s4 = Elite("Samurai",1)

s1.info()
s2.info()
s3.info()
s4.info()
