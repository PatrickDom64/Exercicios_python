import os

os.system('cls')

carros = [ ["Modelo","HRV"],
           ["fabricante","Honda"],
           ["ano","2010"]
]

carros.append(["Cor", "Prata"])

for l,c in carros:
    print("Linha:",l,"| Coluna:",c,"\n")
