import os 
os.system('cls')

valores = [1,5,3,2]

def soma(num):
    r=0
    for n in num:
        r+=n
    return r    
print("Valores:", valores, "Somados:", soma(valores))