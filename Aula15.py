import os

os.system("cls")

#Key - Value
carros={    
            "Fabricante":"honda", 
            "modelo":"HRV",
            "Ano":"2019",
            "Cor":"Prata" 
        }

fab= carros.get("Fabricante")

print(carros["Fabricante"],"\n")
print(fab,"\n")

for x in carros:
    #print(x) #Key
    print(carros[x]) #Value

print("\n")
for c,v in carros.items():
    print(c,": ",v)    

print("\n")
print("Tamanho do Dictionery: ",str(len(carros)))

if "modelo" in carros:
    print("Sim, modelo é uma chave")