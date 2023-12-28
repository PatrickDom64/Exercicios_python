import random
import os

os.system('cls')

erros = 0
sorteador = random.randrange(0,100)
jogador = int(input("Digite um numero:"))

while(sorteador!=jogador):
    os.system('cls')
    if(sorteador>jogador):
        print("Erro, o numero é maior!")
    elif(sorteador<jogador):
        print("Erro, o numero é menor")
    erros+=1
    jogador = int(input("Digite seu numero:"))
print("Numero"+str(jogador), ",voce acertou em ", str(erros+1), "Tentativas")

