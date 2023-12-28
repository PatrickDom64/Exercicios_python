import os

os.system("cls")

#Key - Value
carros={    
    "Carro1":{
            "Fabricante":"honda", 
            "modelo":"HRV"
    },
    "Carro2":{
        "Fabricante":"honda", 
            "modelo":"Civic"
    },
    "Carro3":{
        "Fabricante":"fiat", 
            "modelo":"Uno"
    }
        }

print(carros["Carro1"]["modelo"])